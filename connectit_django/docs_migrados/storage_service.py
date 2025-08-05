"""
Serviço de Camada de Abstração para o Firebase Cloud Storage.

Este módulo encapsula toda a lógica de interação com o bucket de armazenamento,
fornecendo funções simples e seguras para fazer upload e excluir ficheiros.
"""

import datetime
import uuid
from typing import Any, Dict, Optional

from firebase_admin import storage
from flask import current_app
from google.api_core import exceptions as google_exceptions
from google.cloud.storage.bucket import Bucket  # Importação correta da classe Bucket
from werkzeug.datastructures import FileStorage
from werkzeug.utils import secure_filename


def _get_storage_bucket() -> Bucket:
    """
    Obtém a instância do bucket de armazenamento do Firebase.

    Esta função tenta retornar o bucket padrão configurado no SDK do Firebase Admin.
    É uma função interna, usada por outras funções do serviço.

    Returns:
        Bucket: A instância do bucket do Firebase Storage.

    Raises:
        ValueError: Se o bucket do Firebase Storage não estiver configurado
                    ou for inacessível.
    """
    try:
        # A configuração do storageBucket é definida na inicialização do app/__init__.py
        return storage.bucket()
    except Exception as e:
        current_app.logger.critical(
            f"Erro crítico: Bucket do Firebase Storage não configurado ou inacessível: {e}",
            exc_info=True
        )
        # Levanta um ValueError para indicar uma falha de configuração que impede o serviço de funcionar
        raise ValueError("Bucket do Firebase Storage não configurado ou inacessível.")


def upload_file_to_storage(
    file: FileStorage, destination_folder: str
) -> Optional[Dict[str, Any]]:
    """
    Faz upload de um ficheiro para uma pasta específica no Firebase Storage.

    Gera um nome de ficheiro único para evitar colisões, torna o ficheiro público
    e retorna um dicionário com os seus metadados essenciais para serem guardados
    juntamente com o registro do ativo no Firestore.

    Args:
        file (FileStorage): O objeto de ficheiro (`werkzeug.datastructures.FileStorage`)
                            obtido diretamente do `request.files` do Flask.
        destination_folder (str): A pasta de destino dentro do bucket do Storage
                                  (ex: 'assets', 'profiles').

    Returns:
        Optional[Dict[str, Any]]: Um dicionário contendo os metadados do ficheiro
                                  (fileName, fileUrl, filePath, contentType, size, createdAt)
                                  em caso de sucesso no upload. Retorna `None` em caso
                                  de falha no upload ou validação.
    """
    if not file or not file.filename:
        current_app.logger.warning("Tentativa de upload de ficheiro sem conteúdo ou nome.")
        return None

    # Verifica a extensão do arquivo usando a configuração global ALLOWED_EXTENSIONS
    # Adicionado tratamento de erro para filename.rsplit (IndexError se não tiver '.')
    try:
        if '.' not in file.filename or \
           file.filename.rsplit('.', 1)[1].lower() not in current_app.config.get('ALLOWED_EXTENSIONS', set()):
            current_app.logger.warning(
                f"Tentativa de upload de ficheiro com extensão não permitida: "
                f"'{file.filename}'."
            )
            return None
    except IndexError: # Caso o filename seja apenas o nome sem extensão (ex: 'documento')
        current_app.logger.warning(f"Nome de ficheiro inválido (sem extensão): '{file.filename}'.")
        return None


    try:
        bucket: Bucket = _get_storage_bucket()
        original_filename: str = secure_filename(file.filename)
        
        # Gerar nome único para o blob para evitar sobrescritas
        unique_filename: str = f"{uuid.uuid4().hex}_{original_filename}"
        blob_path: str = f"{destination_folder}/{unique_filename}"

        blob = bucket.blob(blob_path)
        
        # Faz o upload do stream do arquivo
        blob.upload_from_file(file.stream, content_type=file.content_type)
        
        # Torna o arquivo publicamente acessível para ser exibido no navegador
        blob.make_public()

        current_app.logger.info(
            f"Ficheiro '{original_filename}' enviado para '{blob_path}' "
            f"com URL: {blob.public_url}"
        )

        return {
            "fileName": original_filename,
            "fileUrl": blob.public_url,
            "filePath": blob_path,  # Caminho interno no bucket para futuras operações
            "contentType": file.content_type,
            "size": blob.size,
            "createdAt": datetime.datetime.now(datetime.timezone.utc)  # Data e hora UTC
        }

    except ValueError as ve:
        # Captura erros específicos do _get_storage_bucket
        current_app.logger.error(f"Erro de configuração do Storage: {ve}", exc_info=True)
        return None
    except google_exceptions.GoogleCloudError as gce:
        # Captura erros gerais da API do Google Cloud (permissões, etc.)
        current_app.logger.error(
            f"Erro na API do Google Cloud Storage durante o upload: {gce}",
            exc_info=True
        )
        return None
    except Exception as e:
        # Captura quaisquer outros erros inesperados durante o upload
        current_app.logger.error(
            f"Erro inesperado durante o upload de ficheiro para o Firebase Storage: {e}",
            exc_info=True
        )
        return None


def delete_file_from_storage(file_path: Optional[str]) -> bool:
    """
    Exclui um ficheiro do Firebase Storage usando o seu caminho completo.

    Args:
        file_path (Optional[str]): O caminho completo do ficheiro dentro do bucket
                                   (obtido do atributo 'filePath' guardado no Firestore).

    Returns:
        bool: True se a exclusão for bem-sucedida ou se o ficheiro não existia
              (e, portanto, não precisou ser excluído). Retorna False se ocorrer
              um erro inesperado durante a tentativa de exclusão.
    """
    if not file_path:
        current_app.logger.warning("Tentativa de excluir ficheiro com caminho vazio.")
        return True  # Considera sucesso, pois o arquivo não existiria de qualquer forma

    try:
        bucket: Bucket = _get_storage_bucket()
        blob = bucket.blob(file_path)
        
        # Verifica se o blob existe antes de tentar deletar para evitar erros desnecessários,
        # embora blob.delete() já lide com NotFound. Esta verificação é mais para logar.
        if not blob.exists():
            current_app.logger.warning(
                f"Tentativa de excluir um ficheiro que não existe no Storage: '{file_path}'."
            )
            return True # Retorna True, pois o objetivo (arquivo não existir) foi atingido

        blob.delete()
        current_app.logger.info(f"Ficheiro '{file_path}' excluído do Storage com sucesso.")
        return True
        
    except ValueError as ve:
        # Captura erros específicos do _get_storage_bucket
        current_app.logger.error(f"Erro de configuração do Storage: {ve}", exc_info=True)
        return False
    except google_exceptions.NotFound:
        # Esta exceção já é tratada pelo Google Cloud Storage se o blob não existe,
        # mas a incluímos explicitamente para log e clareza, retornando True.
        current_app.logger.warning(
            f"Ficheiro '{file_path}' não encontrado no Storage. Nenhuma ação necessária."
        )
        return True
    except google_exceptions.GoogleCloudError as gce:
        current_app.logger.error(
            f"Erro na API do Google Cloud Storage durante a exclusão de '{file_path}': {gce}",
            exc_info=True
        )
        return False
    except Exception as e:
        current_app.logger.error(
            f"Erro inesperado ao excluir o ficheiro '{file_path}' do Storage: {e}",
            exc_info=True
        )
        return False
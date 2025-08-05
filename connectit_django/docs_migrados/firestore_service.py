# app/services/firestore_service.py

"""
Módulo de serviço para interagir com o Google Cloud Firestore.

Fornece funções utilitárias para operações CRUD (Criar, Ler, Atualizar, Excluir)
e funcionalidades de consulta em coleções do Firestore.
"""

import datetime
from typing import Any, Dict, List, Optional, Union

# --- CORREÇÃO APLICADA AQUI: Importação que faltava ---
from google.cloud.firestore_v1.base_query import FieldFilter

import firebase_admin
from firebase_admin import firestore
from flask import current_app


def get_db() -> firestore.Client:
    """
    Retorna a instância do cliente Firestore.
    """
    if not firebase_admin._apps:
        raise RuntimeError(
            "O SDK do Firebase Admin não foi inicializado. "
            "Verifique a configuração em app/__init__.py."
        )
    return firestore.client()


def get_all_documents(collection_name: str) -> List[Dict[str, Any]]:
    """
    Busca todos os documentos de uma coleção específica no Firestore.
    """
    try:
        db = get_db()
        docs_stream = db.collection(collection_name).stream()
        documents: List[Dict[str, Any]] = []
        for doc in docs_stream:
            data = doc.to_dict()
            if data:
                data['id'] = doc.id
                documents.append(data)
        return documents
    except Exception as e:
        current_app.logger.error(
            f"Erro ao buscar todos os documentos da coleção '{collection_name}': {e}",
            exc_info=True
        )
        return []


def get_document(collection_name: str, doc_id: str) -> Optional[Dict[str, Any]]:
    """
    Busca um único documento em uma coleção pelo seu ID.
    """
    if not doc_id:
        current_app.logger.warning(
            f"Tentativa de buscar documento em '{collection_name}' com ID vazio."
        )
        return None
    try:
        db = get_db()
        doc_ref = db.collection(collection_name).document(doc_id)
        doc = doc_ref.get()
        if doc.exists:
            data = doc.to_dict()
            if data:
                data['id'] = doc.id
                return data
        return None
    except Exception as e:
        current_app.logger.error(
            f"Erro ao buscar documento '{doc_id}' na coleção '{collection_name}': {e}",
            exc_info=True
        )
        return None


def add_document(collection_name: str, data: Dict[str, Any]) -> Optional[str]:
    """
    Adiciona um novo documento a uma coleção e retorna o seu ID gerado automaticamente.
    """
    if not data:
        current_app.logger.warning(
            f"Tentativa de adicionar documento vazio na coleção '{collection_name}'."
        )
        return None
    try:
        db = get_db()
        _, doc_ref = db.collection(collection_name).add(data)
        current_app.logger.info(
            f"Documento adicionado com ID '{doc_ref.id}' na coleção '{collection_name}'."
        )
        return doc_ref.id
    except Exception as e:
        current_app.logger.error(
            f"Erro ao adicionar documento na coleção '{collection_name}': {e}",
            exc_info=True
        )
        return None


def update_document(collection_name: str, doc_id: str, data: Dict[str, Any]) -> bool:
    """
    Atualiza campos de um documento existente em uma coleção.
    """
    if not doc_id or not data:
        current_app.logger.warning(
            f"Tentativa de atualizar documento em '{collection_name}' com ID ou dados vazios."
        )
        return False
    try:
        db = get_db()
        db.collection(collection_name).document(doc_id).update(data)
        current_app.logger.info(
            f"Documento '{doc_id}' atualizado na coleção '{collection_name}'."
        )
        return True
    except Exception as e:
        current_app.logger.error(
            f"Erro ao atualizar documento '{doc_id}' na coleção '{collection_name}': {e}",
            exc_info=True
        )
        return False


def delete_document(collection_name: str, doc_id: str) -> bool:
    """
    Exclui um documento de uma coleção.
    """
    if not doc_id:
        current_app.logger.warning(
            f"Tentativa de excluir documento em '{collection_name}' com ID vazio."
        )
        return False
    try:
        db = get_db()
        db.collection(collection_name).document(doc_id).delete()
        current_app.logger.info(
            f"Documento '{doc_id}' excluído da coleção '{collection_name}'."
        )
        return True
    except Exception as e:
        current_app.logger.error(
            f"Erro ao excluir documento '{doc_id}' da coleção '{collection_name}': {e}",
            exc_info=True
        )
        return False


def get_collection_ref(collection_name: str) -> firestore.CollectionReference:
    """
    Retorna a referência de uma coleção específica.
    """
    return get_db().collection(collection_name)


def set_document(collection_name: str, doc_id: str, data: Dict[str, Any]) -> bool:
    """
    Define (sobrescreve) um documento com um ID específico em uma coleção.
    """
    if not doc_id or not data:
        current_app.logger.warning(
            f"Tentativa de definir documento em '{collection_name}' com ID ou dados vazios."
        )
        return False
    try:
        get_collection_ref(collection_name).document(doc_id).set(data)
        current_app.logger.info(
            f"Documento '{doc_id}' definido na coleção '{collection_name}'."
        )
        return True
    except Exception as e:
        current_app.logger.error(
            f"Erro ao definir documento '{doc_id}' na coleção '{collection_name}': {e}",
            exc_info=True
        )
        return False


def query_documents(
    collection_name: str, field: str, operator: str, value: Any
) -> List[Dict[str, Any]]:
    """
    Realiza uma consulta em uma coleção com um filtro simples (campo, operador, valor).
    """
    try:
        docs_stream = get_collection_ref(collection_name).where(field, operator, value).stream()
        documents: List[Dict[str, Any]] = []
        for doc in docs_stream:
            doc_data = doc.to_dict()
            if doc_data:
                doc_data['id'] = doc.id
                documents.append(doc_data)
        return documents
    except Exception as e:
        current_app.logger.error(
            f"Erro ao executar a consulta na coleção '{collection_name}' "
            f"com '{field} {operator} {value}': {e}",
            exc_info=True
        )
        return []


def get_documents_by_query(
    collection_name: str, field: str, operator: str, value: Any
) -> List[Dict[str, Any]]:
    """
    Busca documentos em uma coleção com base em uma consulta 'where', com tratamento de erros.
    """
    try:
        db = get_db()
        collection_ref = db.collection(collection_name)
        query = collection_ref.where(field, operator, value)
        docs_stream = query.stream()

        documents: List[Dict[str, Any]] = []
        for doc in docs_stream:
            doc_data = doc.to_dict()
            if doc_data:
                doc_data['id'] = doc.id
                documents.append(doc_data)

        return documents
    except Exception as e:
        current_app.logger.error(
            f"Erro ao executar a consulta em '{collection_name}' "
            f"({field} {operator} {value}): {e}",
            exc_info=True
        )
        return []


# Em app/services/firestore_service.py, substitua a função existente por esta:

def get_documents_with_query(
    collection_name: str, 
    query_params: List[Dict[str, Any]], 
    limit: Optional[int] = None,
    order_by: Optional[str] = None,
    direction: str = 'asc'
) -> List[Dict[str, Any]]:
    """
    Busca documentos numa coleção com base em múltiplos parâmetros de query,
    com capacidade de ordenação.
    """
    try:
        db = get_db()
        query = db.collection(collection_name)

        for param in query_params:
            query = query.where(filter=FieldFilter(param['field'], param['op'], param['value']))
        
        # --- NOVA LÓGICA DE ORDENAÇÃO ---
        if order_by:
            sort_direction = firestore.Query.ASCENDING if direction == 'asc' else firestore.Query.DESCENDING
            query = query.order_by(order_by, direction=sort_direction)
        
        if limit:
            query = query.limit(limit)

        docs_stream = query.stream()
        documents: List[Dict[str, Any]] = []
        for doc in docs_stream:
            doc_data = doc.to_dict()
            if doc_data:
                doc_data['id'] = doc.id
                documents.append(doc_data)
        return documents
    except Exception as e:
        current_app.logger.error(
            f"Erro ao executar consulta múltipla na coleção '{collection_name}': {e}",
            exc_info=True
        )
        return []

def get_collection_size(collection_name: str) -> int:
    """
    Retorna o número total de documentos numa coleção de forma eficiente.
    """
    try:
        db = get_db()
        count_query = db.collection(collection_name).count()
        result = count_query.get()
        
        if result and result[0]:
            return result[0][0].value
        return 0
    except Exception as e:
        current_app.logger.error(
            f"Erro ao contar documentos na coleção '{collection_name}': {e}",
            exc_info=True
        )
        return 0
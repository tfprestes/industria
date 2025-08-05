# app/routes/supplier_routes.py

"""
Módulo de rotas para a gestão de Fornecedores.

Este blueprint define os endpoints para todas as operações CRUD para a entidade 
'Fornecedores', incluindo a gestão de anexos (upload de ficheiros).
"""

import datetime
import json
import os
from typing import Any, Dict, List, Optional

from firebase_admin import firestore
from flask import (Blueprint, Response, current_app, flash, redirect,
                   render_template, request, session, url_for)
from werkzeug.utils import secure_filename
from werkzeug.wrappers import Response as WerkzeugResponse

from app.auth.routes import login_required, role_required
from app.services.firestore_service import (add_document, delete_document,
                                            get_all_documents, get_document,
                                            get_documents_by_query,
                                            update_document)
from app.models.supplier import Supplier

# O blueprint é definido com um prefixo de URL para este módulo.
# Nota: Este blueprint precisará ser registado no app/__init__.py.
supplier_bp = Blueprint(
    'suppliers',
    __name__,
    url_prefix='/suppliers'
)


def allowed_file(filename: str) -> bool:
    """
    Verifica se a extensão do ficheiro é permitida com base na configuração da app.
    
    Args:
        filename (str): O nome do ficheiro a ser verificado.
        
    Returns:
        bool: True se a extensão for permitida, False caso contrário.
    """
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in current_app.config['ALLOWED_EXTENSIONS']


@supplier_bp.route('/')
@login_required
@role_required('admin', 'viewer')
def list_suppliers() -> str:
    """
    Exibe a lista de todos os Fornecedores.
    
    Returns:
        str: O template da lista de fornecedores renderizado.
    """
    try:
        suppliers: List[Dict[str, Any]] = get_all_documents('suppliers')
        return render_template('settings/suppliers_list.html', suppliers=suppliers)
    except Exception as e:
        current_app.logger.error(f"Erro ao listar fornecedores: {e}", exc_info=True)
        flash("Ocorreu um erro crítico ao carregar os dados dos fornecedores.", "danger")
        return render_template('settings/suppliers_list.html', suppliers=[])


@supplier_bp.route('/form', methods=['GET'])
@supplier_bp.route('/form/<string:supplier_id>', methods=['GET'])
@login_required
@role_required('admin')
def supplier_form(supplier_id: Optional[str] = None) -> str | WerkzeugResponse:
    """
    Exibe um formulário unificado para adicionar ou editar um Fornecedor.

    Args:
        supplier_id (Optional[str]): O ID do fornecedor a ser editado.
                                     Se None, exibe um formulário em branco.
    
    Returns:
        Union[str, WerkzeugResponse]: O template do formulário renderizado ou um
                                      redirecionamento se o ID não for encontrado.
    """
    try:
        supplier: Dict[str, Any] = get_document('suppliers', supplier_id) if supplier_id else {}
        if supplier_id and not supplier:
            flash('Fornecedor não encontrado.', 'danger')
            return redirect(url_for('suppliers.list_suppliers'))
        
        return render_template('settings/supplier_form.html', supplier=supplier)
    except Exception as e:
        current_app.logger.error(f"Erro ao carregar formulário de fornecedor: {e}", exc_info=True)
        flash("Ocorreu um erro ao carregar o formulário.", "danger")
        return redirect(url_for('suppliers.list_suppliers'))


@supplier_bp.route('/save/', methods=['POST'])
@supplier_bp.route('/save/<string:supplier_id>', methods=['POST'])
@login_required
@role_required('admin')
def save_supplier(supplier_id: Optional[str] = None) -> WerkzeugResponse:
    """
    Processa a submissão do formulário para criar ou atualizar um Fornecedor,
    incluindo o upload de ficheiros de anexo.

    Args:
        supplier_id (Optional[str]): O ID do fornecedor a ser atualizado.
                                     Se None, cria um novo.

    Returns:
        WerkzeugResponse: Um redirecionamento para a lista de fornecedores.
    """
    try:
        form_data: Dict[str, Any] = request.form
        if not form_data.get('name'):
            flash('O nome do fornecedor é obrigatório.', 'danger')
            return render_template('settings/supplier_form.html', supplier=dict(form_data))

        # --- Lógica de Upload de Anexos ---
        uploaded_files_info: List[Dict[str, Any]] = []
        files: List[Any] = request.files.getlist('attachment_files')
        for file in files:
            if file and file.filename and allowed_file(file.filename):
                original_filename = secure_filename(file.filename)
                timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S_%f')
                new_filename = f"{timestamp}_{original_filename}"
                
                upload_path = os.path.join(current_app.config['UPLOAD_FOLDER'], 'suppliers')
                os.makedirs(upload_path, exist_ok=True)
                file.save(os.path.join(upload_path, new_filename))

                uploaded_files_info.append({
                    'fileName': original_filename,
                    'fileUrl': f"uploads/suppliers/{new_filename}",
                    'uploadDate': datetime.datetime.now(datetime.timezone.utc),
                    'uploadedBy': session.get('user_email', 'unknown')
                })
        
        # --- Construção dos Dados para Salvar ---
        data_to_save: Dict[str, Any] = {'name': form_data.get('name')}
        optional_fields = ['contactPerson', 'phone', 'email', 'cnpj']
        for field in optional_fields:
            value = form_data.get(field.lower()) # Formulário usa snake_case
            if value:
                data_to_save[field] = value
            elif supplier_id:
                data_to_save[field] = firestore.DELETE_FIELD
        
        existing_attachments = []
        if supplier_id:
            existing_doc = get_document('suppliers', supplier_id)
            if existing_doc: existing_attachments = existing_doc.get('attachments', [])
        
        data_to_save['attachments'] = existing_attachments + uploaded_files_info

        # --- Salvar no Banco de Dados ---
        if supplier_id:
            update_document('suppliers', supplier_id, data_to_save)
            flash(f'Fornecedor "{data_to_save["name"]}" atualizado com sucesso!', 'success')
        else:
            add_document('suppliers', data_to_save)
            flash(f'Fornecedor "{data_to_save["name"]}" criado com sucesso!', 'success')

    except Exception as e:
        current_app.logger.error(f"Erro ao salvar fornecedor: {e}", exc_info=True)
        flash('Ocorreu um erro inesperado ao salvar o fornecedor.', 'danger')

    return redirect(url_for('suppliers.list_suppliers'))


@supplier_bp.route('/delete/<string:supplier_id>', methods=['POST'])
@login_required
@role_required('admin')
def delete_supplier(supplier_id: str) -> WerkzeugResponse:
    """
    Exclui um Fornecedor, após verificar se não há dependências em Ativos.

    Args:
        supplier_id (str): O ID do fornecedor a ser excluído.

    Returns:
        WerkzeugResponse: Um redirecionamento para a lista de fornecedores.
    """
    try:
        # Verificação de dependência: impede a exclusão se estiver em uso por algum ativo.
        dependent_assets = get_documents_by_query('assets', 'supplierId', '==', supplier_id)
        if dependent_assets:
            flash(f'Este fornecedor não pode ser excluído pois está associado a {len(dependent_assets)} ativo(s).', 'danger')
            return redirect(url_for('suppliers.list_suppliers'))

        supplier = get_document('suppliers', supplier_id)
        if not supplier:
            flash('Fornecedor não encontrado.', 'danger')
        else:
            # TODO: Adicionar lógica para apagar os ficheiros de anexo do disco.
            delete_document('suppliers', supplier_id)
            flash(f'Fornecedor "{supplier.get("name")}" excluído com sucesso!', 'success')
            
    except Exception as e:
        current_app.logger.error(f"Erro ao excluir fornecedor {supplier_id}: {e}", exc_info=True)
        flash('Erro ao excluir o fornecedor.', 'danger')
        
    return redirect(url_for('suppliers.list_suppliers'))
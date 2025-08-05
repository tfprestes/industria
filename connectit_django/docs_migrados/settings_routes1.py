# app/routes/settings_routes.py
from flask import Blueprint, render_template, request, redirect, url_for, flash, current_app
from app.auth.routes import login_required, role_required # Importa os decoradores
from app.services.firestore_service import get_all_documents, add_document, get_document, update_document, delete_document # Importa serviços do Firestore
from app.models.sector import Sector # Importa o modelo Sector
from app.models.cost_center import CostCenter # Importa o modelo CostCenter
from app.models.unit import Unit # Importa o modelo Unit
from app.models.supplier import Supplier # Importa o modelo Supplier

settings_bp = Blueprint('settings', __name__)

@settings_bp.route('/sectors', methods=['GET', 'POST'])
@login_required # Garante que apenas utilizadores logados acedam
@role_required('admin') # Garante que apenas administradores acedam
def manage_sectors():
    """
    Lida com a listagem e adição de setores, incluindo a associação a Centros de Custo.
    """
    current_app.logger.debug(f"Método da requisição para /settings/sectors: {request.method}")

    # Buscar Centros de Custo para popular o dropdown no formulário de adição/edição
    all_cost_centers_data = get_all_documents('costCenters')
    cost_centers = [CostCenter.from_dict(cc_data, id=cc_data['id']) for cc_data in all_cost_centers_data]
    
    # Dicionário para mapear IDs de Centro de Custo para nomes (para exibição na tabela)
    cost_center_names = {cc.id: cc.name for cc in cost_centers}

    if request.method == 'POST':
        # Lógica para ADICIONAR NOVO SETOR (POST para a mesma rota)
        sector_name = request.form.get('name')
        sector_description = request.form.get('description')
        associated_cost_center_id = request.form.get('associated_cost_center_id')

        current_app.logger.debug(f"Dados do POST para setor: Nome={sector_name}, Descrição={sector_description}, CentroCustoID={associated_cost_center_id}")

        if not sector_name:
            flash('O nome do setor é obrigatório.', 'error')
        elif not associated_cost_center_id:
            flash('O Centro de Custo Associado é obrigatório.', 'error')
        else:
            new_sector_data = {
                'name': sector_name,
                'description': sector_description,
                'associatedCostCenterId': associated_cost_center_id
            }
            try:
                sector_id = add_document('sectors', new_sector_data)
                flash(f'Setor "{sector_name}" adicionado com sucesso! ID: {sector_id}', 'success')
                return redirect(url_for('settings.manage_sectors'))
            except Exception as e:
                current_app.logger.error(f"Erro ao adicionar setor: {e}")
                flash(f'Erro ao adicionar setor: {e}', 'error')

    # Para requisições GET ou após POST sem sucesso
    sectors = get_all_documents('sectors') # Busca todos os setores do Firestore
    
    # Mapear os setores para incluir o nome do Centro de Custo associado para exibição
    for sector in sectors:
        if sector.get('associatedCostCenterId'):
            sector['associatedCostCenterName'] = cost_center_names.get(sector['associatedCostCenterId'], 'Não Encontrado')
        else:
            sector['associatedCostCenterName'] = 'Nenhum'
            
    # Passamos também os centros de custo para o formulário de adição na mesma página
    return render_template('settings/sectors_list.html', sectors=sectors, cost_centers=cost_centers)


@settings_bp.route('/sectors/edit/<string:sector_id>', methods=['GET', 'POST'])
@login_required
@role_required('admin')
def edit_sector(sector_id):
    """
    Lida com a edição de um Setor específico.
    """
    sector_data = get_document('sectors', sector_id)
    if not sector_data:
        flash('Setor não encontrado.', 'error')
        return redirect(url_for('settings.manage_sectors'))

    sector = Sector.from_dict(sector_data, id=sector_id)

    # Buscar Centros de Custo para popular o dropdown no formulário de edição
    all_cost_centers_data = get_all_documents('costCenters')
    cost_centers = [CostCenter.from_dict(cc_data, id=cc_data['id']) for cc_data in all_cost_centers_data]

    if request.method == 'POST':
        sector_name = request.form.get('name')
        sector_description = request.form.get('description')
        associated_cost_center_id = request.form.get('associated_cost_center_id')

        if not sector_name:
            flash('O nome do setor é obrigatório.', 'error')
        elif not associated_cost_center_id:
            flash('O Centro de Custo Associado é obrigatório.', 'error')
        else:
            updated_data = {
                'name': sector_name,
                'description': sector_description,
                'associatedCostCenterId': associated_cost_center_id
            }
            try:
                update_document('sectors', sector_id, updated_data)
                flash(f'Setor "{sector_name}" atualizado com sucesso!', 'success')
                return redirect(url_for('settings.manage_sectors'))
            except Exception as e:
                flash(f'Erro ao atualizar setor: {e}', 'error')

    # Para requisições GET ou POST com falha na validação
    return render_template('settings/sector_form.html', sector=sector, cost_centers=cost_centers)


@settings_bp.route('/sectors/delete/<string:sector_id>', methods=['POST'])
@login_required
@role_required('admin')
def delete_sector(sector_id):
    """
    Lida com a exclusão de um Setor específico.
    """
    try:
        delete_document('sectors', sector_id)
        flash('Setor excluído com sucesso!', 'success')
    except Exception as e:
        flash(f'Erro ao excluir setor: {e}', 'error')
    return redirect(url_for('settings.manage_sectors'))


# --- Rotas para Gestão de Unidades ---
@settings_bp.route('/units', methods=['GET', 'POST'])
@login_required
@role_required('admin')
def manage_units():
    """
    Lida com a listagem e adição de unidades.
    """
    if request.method == 'POST':
        unit_name = request.form.get('name')
        unit_type = request.form.get('type')
        unit_cnpj = request.form.get('cnpj')
        address_street = request.form.get('address_street')
        address_number = request.form.get('address_number')
        address_complement = request.form.get('address_complement')
        address_neighborhood = request.form.get('address_neighborhood')
        address_city = request.form.get('address_city')
        address_state = request.form.get('address_state')
        address_zip_code = request.form.get('address_zip_code')
        address_country = request.form.get('address_country')
        unit_description = request.form.get('description')

        if not unit_name or not unit_type or not address_city or not address_state or not address_country:
            flash('Nome, Tipo, Cidade, Estado e País são campos obrigatórios para a Unidade.', 'error')
        else:
            new_unit_data = {
                'name': unit_name,
                'type': unit_type,
                'cnpj': unit_cnpj,
                'address': {
                    'street': address_street,
                    'number': address_number,
                    'complement': address_complement,
                    'neighborhood': address_neighborhood,
                    'city': address_city,
                    'state': address_state,
                    'zipCode': address_zip_code,
                    'country': address_country
                },
                'description': unit_description
            }
            try:
                unit_id = add_document('units', new_unit_data)
                flash(f'Unidade "{unit_name}" adicionada com sucesso! ID: {unit_id}', 'success')
                return redirect(url_for('settings.manage_units'))
            except Exception as e:
                current_app.logger.error(f"Erro ao adicionar unidade: {e}")
                flash(f'Erro ao adicionar unidade: {e}', 'error')

    units = get_all_documents('units')
    return render_template('settings/units_list.html', units=units)

@settings_bp.route('/units/edit/<string:unit_id>', methods=['GET', 'POST'])
@login_required
@role_required('admin')
def edit_unit(unit_id):
    """
    Lida com a edição de uma Unidade específica.
    """
    unit_data = get_document('units', unit_id)
    if not unit_data:
        flash('Unidade não encontrada.', 'error')
        return redirect(url_for('settings.manage_units'))
    
    unit = Unit.from_dict(unit_data, id=unit_id)

    if request.method == 'POST':
        unit_name = request.form.get('name')
        unit_type = request.form.get('type')
        unit_cnpj = request.form.get('cnpj')
        address_street = request.form.get('address_street')
        address_number = request.form.get('address_number')
        address_complement = request.form.get('address_complement')
        address_neighborhood = request.form.get('address_neighborhood')
        address_city = request.form.get('address_city')
        address_state = request.form.get('address_state')
        address_zip_code = request.form.get('address_zip_code')
        address_country = request.form.get('address_country')
        unit_description = request.form.get('description')

        if not unit_name or not unit_type or not address_city or not address_state or not address_country:
            flash('Nome, Tipo, Cidade, Estado e País são campos obrigatórios para a Unidade.', 'error')
        else:
            updated_data = {
                'name': unit_name,
                'type': unit_type,
                'cnpj': unit_cnpj,
                'address': {
                    'street': address_street,
                    'number': address_number,
                    'complement': address_complement,
                    'neighborhood': address_neighborhood,
                    'city': address_city,
                    'state': address_state,
                    'zipCode': address_zip_code,
                    'country': address_country
                },
                'description': unit_description
            }
            try:
                update_document('units', unit_id, updated_data)
                flash(f'Unidade "{unit_name}" atualizada com sucesso!', 'success')
                return redirect(url_for('settings.manage_units'))
            except Exception as e:
                flash(f'Erro ao atualizar unidade: {e}', 'error')

    return render_template('settings/unit_form.html', unit=unit)


@settings_bp.route('/units/delete/<string:unit_id>', methods=['POST'])
@login_required
@role_required('admin')
def delete_unit(unit_id):
    """
    Lida com a exclusão de uma Unidade específica.
    """
    try:
        delete_document('units', unit_id)
        flash('Unidade excluída com sucesso!', 'success')
    except Exception as e:
        flash(f'Erro ao excluir Unidade: {e}', 'error')
    return redirect(url_for('settings.manage_units'))


@settings_bp.route('/cost_centers', methods=['GET', 'POST'])
@login_required
@role_required('admin')
def manage_cost_centers():
    """
    Lida com a listagem e adição de Centros de Custo.
    """
    if request.method == 'POST':
        cc_name = request.form.get('name')
        cc_description = request.form.get('description')

        if not cc_name:
            flash('O nome do Centro de Custo é obrigatório.', 'error')
        else:
            new_cc_data = {
                'name': cc_name,
                'description': cc_description
            }
            try:
                cc_id = add_document('costCenters', new_cc_data)
                flash(f'Centro de Custo "{cc_name}" adicionado com sucesso! ID: {cc_id}', 'success')
                return redirect(url_for('settings.manage_cost_centers'))
            except Exception as e:
                flash(f'Erro ao adicionar Centro de Custo: {e}', 'error')

    cost_centers = get_all_documents('costCenters') # Busca todos os centros de custo
    return render_template('settings/cost_centers_list.html', cost_centers=cost_centers)


@settings_bp.route('/cost_centers/edit/<string:cc_id>', methods=['GET', 'POST'])
@login_required
@role_required('admin')
def edit_cost_center(cc_id):
    """
    Lida com a edição de um Centro de Custo específico.
    """
    cost_center_data = get_document('costCenters', cc_id)
    if not cost_center_data:
        flash('Centro de Custo não encontrado.', 'error')
        return redirect(url_for('settings.manage_cost_centers'))

    cost_center = CostCenter.from_dict(cost_center_data, id=cc_id)

    if request.method == 'POST':
        cc_name = request.form.get('name')
        cc_description = request.form.get('description')

        if not cc_name:
            flash('O nome do Centro de Custo é obrigatório.', 'error')
        else:
            updated_data = {
                'name': cc_name,
                'description': cc_description
            }
            try:
                update_document('costCenters', cc_id, updated_data)
                flash(f'Centro de Custo "{cc_name}" atualizado com sucesso!', 'success')
                return redirect(url_for('settings.manage_cost_centers'))
            except Exception as e:
                flash(f'Erro ao atualizar Centro de Custo: {e}', 'error')

    return render_template('settings/cost_center_form.html', cost_center=cost_center)


@settings_bp.route('/cost_centers/delete/<string:cc_id>', methods=['POST'])
@login_required
@role_required('admin')
def delete_cost_center(cc_id):
    """
    Lida com a exclusão de um Centro de Custo específico.
    """
    try:
        delete_document('costCenters', cc_id)
        flash('Centro de Custo excluído com sucesso!', 'success')
    except Exception as e:
        flash(f'Erro ao excluir Centro de Custo: {e}', 'error')
    return redirect(url_for('settings.manage_cost_centers'))


# --- Rotas para Gestão de Fornecedores ---
@settings_bp.route('/suppliers', methods=['GET', 'POST'])
@login_required
@role_required('admin')
def manage_suppliers():
    """
    Lida com a listagem e adição de fornecedores.
    """
    if request.method == 'POST':
        supplier_name = request.form.get('name')
        contact_person = request.form.get('contact_person')
        phone = request.form.get('phone')
        email = request.form.get('email')
        cnpj = request.form.get('cnpj')

        if not supplier_name:
            flash('O nome do fornecedor é obrigatório.', 'error')
        else:
            new_supplier_data = {
                'name': supplier_name,
                'contactPerson': contact_person,
                'phone': phone,
                'email': email,
                'cnpj': cnpj
            }
            try:
                supplier_id = add_document('suppliers', new_supplier_data)
                flash(f'Fornecedor "{supplier_name}" adicionado com sucesso! ID: {supplier_id}', 'success')
                return redirect(url_for('settings.manage_suppliers'))
            except Exception as e:
                current_app.logger.error(f"Erro ao adicionar fornecedor: {e}")
                flash(f'Erro ao adicionar fornecedor: {e}', 'error')

    suppliers = get_all_documents('suppliers')
    return render_template('settings/suppliers_list.html', suppliers=suppliers)

@settings_bp.route('/suppliers/edit/<string:supplier_id>', methods=['GET', 'POST'])
@login_required
@role_required('admin')
def edit_supplier(supplier_id):
    """
    Lida com a edição de um Fornecedor específico.
    """
    supplier_data = get_document('suppliers', supplier_id)
    if not supplier_data:
        flash('Fornecedor não encontrado.', 'error')
        return redirect(url_for('settings.manage_suppliers'))
    
    supplier = Supplier.from_dict(supplier_data, id=supplier_id)

    if request.method == 'POST':
        supplier_name = request.form.get('name')
        contact_person = request.form.get('contact_person')
        phone = request.form.get('phone')
        email = request.form.get('email')
        cnpj = request.form.get('cnpj')

        if not supplier_name:
            flash('O nome do fornecedor é obrigatório.', 'error')
        else:
            updated_data = {
                'name': supplier_name,
                'contactPerson': contact_person,
                'phone': phone,
                'email': email,
                'cnpj': cnpj
            }
            try:
                update_document('suppliers', supplier_id, updated_data)
                flash(f'Fornecedor "{supplier_name}" atualizado com sucesso!', 'success')
                return redirect(url_for('settings.manage_suppliers'))
            except Exception as e:
                flash(f'Erro ao atualizar fornecedor: {e}', 'error')

    return render_template('settings/supplier_form.html', supplier=supplier)

@settings_bp.route('/suppliers/delete/<string:supplier_id>', methods=['POST'])
@login_required
@role_required('admin')
def delete_supplier(supplier_id):
    """
    Lida com a exclusão de um Fornecedor específico.
    """
    try:
        delete_document('suppliers', supplier_id)
        flash('Fornecedor excluído com sucesso!', 'success')
    except Exception as e:
        flash(f'Erro ao excluir Fornecedor: {e}', 'error')
    return redirect(url_for('settings.manage_suppliers'))


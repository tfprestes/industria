# app/auth/routes.py

from flask import Blueprint, render_template, request, redirect, url_for, flash, session, current_app
from functools import wraps
from app.auth.services import authenticate_user, register_user
from app.services.firestore_service import get_collection_ref

auth_bp = Blueprint('auth', __name__)

# --- Decoradores de Autenticação e Permissão ---

def login_required(f):
    """
    Decorador para rotas que exigem que o utilizador esteja logado.
    Redireciona para a página de login se não houver utilizador na sessão.
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash('Você precisa estar logado para acessar esta página.', 'warning')
            return redirect(url_for('auth.login', next=request.url))
        return f(*args, **kwargs)
    return decorated_function

def role_required(*roles):
    """
    Decorador para rotas que exigem um ou mais perfis específicos.
    Utiliza o login_required e verifica se a role do utilizador na sessão
    está contida na lista de roles permitidas.
    Ex: @role_required('admin')
    Ex: @role_required('admin', 'viewer')
    """
    def decorator(f):
        @wraps(f)
        @login_required  # Garante que o utilizador esteja logado primeiro
        def decorated_function(*args, **kwargs):
            user_role = session.get('user_role', 'viewer') # Pega a role da sessão
            if user_role not in roles:
                flash(f'Acesso negado. Sua permissão de "{user_role}" não é suficiente para aceder a esta página.', 'danger')
                # Redireciona para o dashboard ou uma página de acesso negado
                return redirect(url_for('dashboard.index'))
            return f(*args, **kwargs)
        return decorated_function
    return decorator


# --- Rotas de Autenticação ---

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    """
    Lida com o login do utilizador.
    Se o utilizador já estiver logado, redireciona para o dashboard.
    """
    if 'user_id' in session:
        return redirect(url_for('dashboard.index'))

    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        success, result = authenticate_user(email, password)
        
        if success:
            user_data = result
            session['user_id'] = user_data['uid']
            session['user_email'] = user_data['email']
            session['user_role'] = user_data.get('role', 'viewer')
            
            flash(f'Bem-vindo(a), {user_data["email"]}!', 'success')
            current_app.logger.info(f"Utilizador {user_data['email']} ({user_data['uid']}) logado. Role: {session['user_role']}")
            
            # Redireciona para a página que o utilizador tentou aceder ou para o dashboard
            next_page = request.args.get('next')
            return redirect(next_page or url_for('dashboard.index'))
        else:
            flash(f'Erro no login: {result}', 'danger')
            current_app.logger.warning(f"Tentativa de login falhou para {email}: {result}")
            return render_template('auth/login.html', email=email)
    
    return render_template('auth/login.html')

@auth_bp.route('/logout')
@login_required
def logout():
    """
    Lida com o logout do utilizador, limpando a sessão.
    """
    user_email = session.get('user_email', 'Desconhecido')
    session.clear() # Limpa toda a sessão de forma segura
    flash(f'Você ({user_email}) foi desconectado(a).', 'info')
    current_app.logger.info(f"Utilizador {user_email} deslogado.")
    return redirect(url_for('auth.login'))

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    """
    Lida com o registo de novos utilizadores.
    Apenas para fins de configuração inicial. Em produção, esta rota pode ser desativada ou protegida.
    """
    if 'user_id' in session:
        flash('Você já está logado.', 'info')
        return redirect(url_for('dashboard.index'))

    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        # Lógica para atribuir 'admin' ao primeiro utilizador registado
        try:
            users_collection_ref = get_collection_ref('users')
            # Verifica se a coleção de utilizadores está vazia
            first_user = not any(users_collection_ref.limit(1).stream())
            role = 'admin' if first_user else 'viewer'
            
            success, result = register_user(email, password, role=role)
            
            if success:
                flash(f'Conta ({email}) criada com sucesso como {role}! Faça login para continuar.', 'success')
                current_app.logger.info(f"Utilizador {email} registado com sucesso. Role: {role}")
                return redirect(url_for('auth.login'))
            else:
                flash(f'Erro ao registar: {result}', 'danger')
                current_app.logger.error(f"Erro ao registar utilizador {email}: {result}")
                return render_template('auth/register.html', email=email)
        
        except Exception as e:
            current_app.logger.critical(f"Falha crítica no registo, possivelmente problema com o Firestore: {e}")
            flash("Ocorreu um erro crítico no sistema. Tente mais tarde.", "danger")
            return render_template('auth/register.html', email=email)
            
    return render_template('auth/register.html')
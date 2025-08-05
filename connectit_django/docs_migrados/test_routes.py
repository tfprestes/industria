# tests/test_routes.py
# Testes para as rotas da aplicação (ex: acessibilidade, respostas HTTP)

import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_login_page(client):
    response = client.get('/auth/login')
    assert response.status_code == 200
    assert b"Login no ConnectIT" in response.data

def test_dashboard_access(client):
    # Por enquanto, o dashboard pode ser acessado sem login
    # No futuro, precisaremos simular um login
    response = client.get('/dashboard/')
    assert response.status_code == 200
    assert b"Dashboard Geral" in response.data

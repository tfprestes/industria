# app/auth/models.py
# Modelos de dados para usuários (se houver extensão do Firebase Auth ou User management local)
class User:
    def __init__(self, uid, email, role='viewer'):
        self.uid = uid
        self.email = email
        self.role = role

    def to_dict(self):
        return {
            "uid": self.uid,
            "email": self.email,
            "role": self.role
        }

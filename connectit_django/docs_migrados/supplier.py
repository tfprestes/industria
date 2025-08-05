# app/models/supplier.py

class Supplier:
    """Representa um fornecedor no sistema."""

    def __init__(self, name, id=None, contact_person=None, phone=None, email=None, cnpj=None, attachments=None):
        """
        Construtor da classe Supplier.
        'name' é o único campo obrigatório para criar um objeto.
        """
        self.id = id
        self.name = name
        self.contact_person = contact_person
        self.phone = phone
        self.email = email
        self.cnpj = cnpj
        # Garante que 'attachments' seja sempre uma lista, nunca None.
        self.attachments = attachments if attachments is not None else []

    def to_dict(self):
        """Converte o objeto para um dicionário para ser salvo no Firestore."""
        return {
            "name": self.name,
            "contactPerson": self.contact_person,
            "phone": self.phone,
            "email": self.email,
            "cnpj": self.cnpj,
            "attachments": self.attachments
        }

    @staticmethod
    def from_dict(source, id=None):
        """
        Cria um objeto Supplier a partir de um dicionário vindo do Firestore.
        """
        # Código formatado para melhor legibilidade e robustez
        return Supplier(
            id=id,
            name=source.get('name'),
            contact_person=source.get('contactPerson'),
            phone=source.get('phone'),
            email=source.get('email'),
            cnpj=source.get('cnpj'),
            # Garante uma lista vazia como padrão se o campo não existir no Firestore
            attachments=source.get('attachments', [])
        )
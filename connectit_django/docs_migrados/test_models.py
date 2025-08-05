# tests/test_models.py
import pytest
from app.models.sector import Sector

def test_sector_to_dict():
    sector = Sector(name="TI", description="Tecnologia da Informação")
    expected_dict = {"name": "TI", "description": "Tecnologia da Informação"}
    assert sector.to_dict() == expected_dict

def test_sector_from_dict():
    data = {"name": "RH", "description": "Recursos Humanos"}
    sector = Sector.from_dict(data, id="123")
    assert sector.id == "123"
    assert sector.name == "RH"
    assert sector.description == "Recursos Humanos"

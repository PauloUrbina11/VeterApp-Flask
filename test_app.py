import pytest
from app import app, db
from models import Veterinarian, Pet

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client


def test_add_vet(client):
    res = client.post('/veterinarians/add', data={'name': 'Dra. Ana'}, follow_redirects=True)
    assert res.status_code == 200
    assert b'Dra. Ana' in res.data

def test_add_pet(client):
    with app.app_context():
        vet = Veterinarian(name='Dr. Carlos')
        db.session.add(vet)
        db.session.commit()
    res = client.post('/pets/add', data={'name': 'Max', 'species': 'Perro', 'vet_id': '1'}, follow_redirects=True)
    assert res.status_code == 200
    assert b'Max' in res.data
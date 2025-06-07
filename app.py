from flask import Flask, render_template, request, redirect, url_for, jsonify
from models import db, Veterinarian, Pet
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///veterapp.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

@app.route('/')
def index():
    return render_template('index.html')

# Veterinarians
@app.route('/veterinarians')
def list_vets():
    vets = Veterinarian.query.all()
    return render_template('vets.html', vets=vets)

@app.route('/veterinarians/add', methods=['POST'])
def add_vet():
    name = request.form['name']
    vet = Veterinarian(name=name)
    db.session.add(vet)
    db.session.commit()
    return redirect(url_for('list_vets'))

# Pets
@app.route('/pets')
def list_pets():
    pets = Pet.query.all()
    vets = Veterinarian.query.all()  # Obtener veterinarios
    return render_template('pets.html', pets=pets, vets=vets)  # Pasar vets al template

@app.route('/pets/add', methods=['POST'])
def add_pet():
    name = request.form['name']
    species = request.form['species']
    vet_id = request.form['vet_id']
    pet = Pet(name=name, species=species, veterinarian_id=vet_id)
    db.session.add(pet)
    db.session.commit()
    return redirect(url_for('list_pets'))

if __name__ == '__main__':
    app.run(debug=True)
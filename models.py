from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Veterinarian(db.Model):
    __tablename__ = 'veterinarians'  # Opcional, para claridad

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    pets = db.relationship('Pet', backref='veterinarian', lazy=True)

    def __repr__(self):
        return f'<Veterinarian {self.name}>'

class Pet(db.Model):
    __tablename__ = 'pets'  # Opcional, para claridad

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    species = db.Column(db.String(100), nullable=False)
    veterinarian_id = db.Column(db.Integer, db.ForeignKey('veterinarians.id'), nullable=False)

    def __repr__(self):
        return f'<Pet {self.name} ({self.species})>'

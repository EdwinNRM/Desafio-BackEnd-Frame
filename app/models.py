from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    cpf = db.Column(db.String(14), unique=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(100))
    balance = db.Column(db.Float, default=0.0)
    is_merchant = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f'<User {self.name}>'
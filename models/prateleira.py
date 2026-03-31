from database import db

class Prateleira(db.Model):

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    nome = db.Column(
        db.String(50),
        nullable=False,
        unique=True
    )

    def __repr__(self):
        return f"<Prateleira {self.nome}>"
from database import db

class Classificacao(db.Model):
    __tablename__ = "classificacao"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    nome_classificacao = db.Column(
        db.String(100),
        nullable=False
    )

    descricao = db.Column(
        db.String(255)
    )
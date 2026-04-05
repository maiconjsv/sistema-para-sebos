from database import db
from datetime import datetime

class Setor(db.Model):
    __tablename__ = "setor"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    nome = db.Column(
        db.String(100),
        nullable=False,
        unique=True
    )

    descricao = db.Column(
        db.String(255)
    )

    ativo = db.Column(
        db.Boolean,
        default=True
    )

    data_criacao = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )
    classificacao = db.Column(
        db.String(100)  
    )


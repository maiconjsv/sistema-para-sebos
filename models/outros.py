from database import db
from datetime import datetime

class Outro(db.Model):

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    nome = db.Column(
        db.String(150),
        nullable=False
    )

    descricao = db.Column(
        db.String(200),
        nullable=False
    )

    data_entrada = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    id_setor = db.Column(
        db.Integer,
        db.ForeignKey("setor.id"),
        nullable=False
    )

    setor = db.relationship(
        "Setor",
        backref="outros"
    )
    
    id_classificacao = db.Column(
        db.Integer,
        db.ForeignKey("classificacao.id"),
        nullable=False
    )

    classificacao = db.relationship(
        "Classificacao",
        backref="outros"
    )
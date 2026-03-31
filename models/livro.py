from database import db
from datetime import datetime

class Livro(db.Model):

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    titulo = db.Column(
        db.String(200),
        nullable=False
    )

    autor = db.Column(
        db.String(150),
        nullable=False
    )

    preco_compra = db.Column(
        db.Float,
        nullable=False
    )

    quantidade = db.Column(
        db.Integer,
        nullable=False
    )

    data_entrada = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    id_prateleira = db.Column(
        db.Integer,
        db.ForeignKey("prateleira.id"),
        nullable=False
    )
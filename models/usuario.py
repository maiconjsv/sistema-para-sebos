from database import db
from datetime import datetime

class Usuario(db.Model):

    id = db.Column(
        db.Integer,
        primary_key=True
    )


    nome = db.Column(
        db.String(100),
        nullable=False
    )

    funcao = db.Column(
        db.String(50),
        nullable=False
    )

    login = db.Column(
        db.String(150),
        unique=True,
        nullable=False
    )

    senha = db.Column(
        db.String(200),
        nullable=False
    )
    
    data_criacao = db.Column(
        db.DateTime, 
        default=datetime.utcnow, 
        nullable=False
    )
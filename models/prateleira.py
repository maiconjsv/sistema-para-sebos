from database import db

##class Prateleira(db.Model):
##
##    id = db.Column(
##        db.Integer,
##        primary_key=True
##   )

##    nome = db.Column(
##        db.String(50),
##        nullable=False,
##       unique=True
##    )

##    def __repr__(self):
##        return f"<Prateleira {self.nome}>"
class Prateleira(db.Model):

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    codigo = db.Column(
        db.String(10),
        unique=True,
        nullable=False
    )

    descricao = db.Column(
        db.String(100)
    )   

    id_setor = db.Column(
        db.Integer,
        db.ForeignKey("setor.id"),
        nullable=False
    )
    setor = db.relationship(
    "Setor",
    backref="prateleiras"
    )
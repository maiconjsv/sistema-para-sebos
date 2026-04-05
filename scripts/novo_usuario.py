from werkzeug.security import generate_password_hash
from database import db
from models.usuario import Usuario

def criar_admin():

    from werkzeug.security import generate_password_hash

    usuario = Usuario(
        nome="Administrador",
        funcao="admin",
        login="adm",
        senha=generate_password_hash("123")
    )

    db.session.add(usuario)
    db.session.commit()
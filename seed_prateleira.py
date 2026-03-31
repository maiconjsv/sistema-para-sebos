from app import app
from database import db
from models.prateleira import Prateleira

with app.app_context():

    prateleira = Prateleira(nome="A1")

    db.session.add(prateleira)
    db.session.commit()

    print("Prateleira criada")
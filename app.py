from flask import Flask
from database import db
from routes.entrada_estoque import entrada_estoque_bp
from routes.listar_produtos import listar_produtos_bp
from routes.cadastro_patreleira import cadastrar_prateleira_bp

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///sebo.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

app.register_blueprint(entrada_estoque_bp)
app.register_blueprint(listar_produtos_bp)  
app.register_blueprint(cadastrar_prateleira_bp)



with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
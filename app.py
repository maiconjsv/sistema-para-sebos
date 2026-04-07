from flask import Flask
from database import db
import os
from flask_migrate import Migrate
from routes.estoque.entrada_outros import  entrada_outros_bp
from routes.estoque.entrada_livro import entrada_livro_bp
from routes.estoque.listar_produtos import listar_produtos_bp
from routes.estoque.cadastro_patreleira import cadastrar_prateleira_bp
from routes.estoque.cadastro_setor import cadastro_setor_bp
from routes.estoque.cadastros_classificacao import cadastro_classificacao_bp
from routes.usuario.login import login_bp
from models.usuario import Usuario
from models.setor import Setor
from models.prateleira import Prateleira
from models.classificacoes import Classificacao

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "dev-secret-key")

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///sebo.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
migrate = Migrate(app, db)

app.register_blueprint(entrada_livro_bp)
app.register_blueprint(listar_produtos_bp)
app.register_blueprint(cadastro_setor_bp)
app.register_blueprint(cadastro_classificacao_bp)
app.register_blueprint(cadastrar_prateleira_bp)
app.register_blueprint(entrada_outros_bp)
app.register_blueprint(login_bp)


##with app.app_context():
##    db.create_all() (com o uso do Flask-Migrate, não é necessário criar as tabelas manualmente)

if __name__ == "__main__":
    app.run(debug=True)
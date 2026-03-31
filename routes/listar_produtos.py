from flask import Blueprint, request, render_template
from database import db
from models.livro import Livro
from models.prateleira import Prateleira


listar_produtos_bp = Blueprint("listar_produtos", __name__)

@listar_produtos_bp.route("/produtos")
def listar_produtos():
    livros = Livro.query.all()
    return render_template(
        "estoque/listar.html",
        livros=livros
    )
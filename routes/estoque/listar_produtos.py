from flask import Blueprint, request, render_template
from auth import login_required
from models.livro import Livro


listar_produtos_bp = Blueprint("listar_produtos", __name__)

@listar_produtos_bp.route("/produtos")

@login_required

def listar_produtos():
    livros = Livro.query.all()
    return render_template(
        "estoque/listar.html",
        livros=livros
    )
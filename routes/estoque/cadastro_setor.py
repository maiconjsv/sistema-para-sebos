from flask import Blueprint, request, render_template
from auth import login_required
from database import db

cadastro_setor_bp = Blueprint("cadastro_setor", __name__)  

@cadastro_setor_bp.route("/cadastro_setor", methods=["GET", "POST"])

@login_required

def cadastro_setor():
    message = ""

    if request.method == "POST":

        nome = request.form.get("nome")
        descricao = request.form.get("descricao")
        classificacao = request.form.get("classificacao")

        if not nome:
            message = "Nome obrigatório"

        else:

            from models.setor import Setor

            setor = Setor(
                nome=nome,
                descricao=descricao,
                classificacao=classificacao
            )

            db.session.add(setor)
            db.session.commit()

            message = "Setor cadastrado com sucesso"

    return render_template(
        "estoque/cadastro_setor.html",
        message=message
    )
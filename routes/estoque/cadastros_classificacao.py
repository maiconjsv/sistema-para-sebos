from flask import Blueprint, request, render_template
from flask_login import login_required
from database import db
from models.classificacoes import Classificacao
from sqlalchemy.exc import IntegrityError

cadastro_classificacao_bp = Blueprint(
    "cadastro_classificacao",
    __name__
)

@cadastro_classificacao_bp.route(
    "/cadastro_classificacao",
    methods=["GET", "POST"]
)

@login_required

def cadastro_classificacao():

    message = ""

    if request.method == "POST":

        nome_classificacao = request.form.get("nome_classificacao")
        descricao = request.form.get("descricao")

        if not nome_classificacao:
            message = "Nome da classificação é obrigatório"

        else:

            classificacao_existente = Classificacao.query.filter_by(
                nome_classificacao=nome_classificacao
            ).first()

            if classificacao_existente:
                message = "Já existe uma classificação com esse nome"

            else:

                classificacao = Classificacao(
                    nome_classificacao=nome_classificacao,
                    descricao=descricao
                )

                try:
                    db.session.add(classificacao)
                    db.session.commit()

                    message = "Classificação cadastrada com sucesso"

                except IntegrityError:
                    db.session.rollback()
                    message = "Erro: classificação já existe"

    classificacoes = Classificacao.query.all()

    return render_template(
        "estoque/cadastro_classificacao.html",
        classificacoes=classificacoes,
        message=message
    )
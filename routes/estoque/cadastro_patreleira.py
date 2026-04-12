from flask import Blueprint, request, render_template, session
from auth import login_required
from database import db
from models.prateleira import Prateleira
from models.setor import Setor

cadastrar_prateleira_bp = Blueprint(
    "cadastrar_prateleira",
    __name__
)

@cadastrar_prateleira_bp.route("/cadastro_prateleira", methods=["GET", "POST"])

@login_required

def cadastrar_prateleira():

    message = ""

    if request.method == "POST":

        codigo = request.form.get("codigo")
        descricao = request.form.get("descricao")
        id_setor = request.form.get("id_setor")

        if not codigo:
            message = "Código obrigatório"

        else:

            prateleira = Prateleira(
                codigo=codigo,
                descricao=descricao,
                id_setor=id_setor
            )

            db.session.add(prateleira)
            db.session.commit()

            message = "Prateleira cadastrada com sucesso"

    prateleiras = Prateleira.query.all()
    setores = Setor.query.all()
    return render_template(
        "estoque/cadastro_prateleira.html",
        prateleiras=prateleiras,
        message=message,
        setores=setores,
        usuario_logado = session["usuario_nome"]
    )
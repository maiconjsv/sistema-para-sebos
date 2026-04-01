from flask import Blueprint, request, render_template
from database import db
from models.prateleira import Prateleira

cadastrar_prateleira_bp = Blueprint(
    "cadastrar_prateleira",
    __name__
)

@cadastrar_prateleira_bp.route("/cadastro_prateleira", methods=["GET", "POST"])
def cadastrar_prateleira():

    message = ""

    if request.method == "POST":

        codigo = request.form.get("codigo")
        descricao = request.form.get("descricao")
        setor = request.form.get("setor")

        if not codigo:
            message = "Código obrigatório"

        else:

            prateleira = Prateleira(
                codigo=codigo,
                descricao=descricao,
                setor=setor
            )

            db.session.add(prateleira)
            db.session.commit()

            message = "Prateleira cadastrada com sucesso"

    prateleiras = Prateleira.query.all()

    return render_template(
        "cadastro_prateleira.html",
        prateleiras=prateleiras,
        message=message
    )
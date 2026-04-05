from flask import Blueprint, request, render_template

from auth import login_required
from database import db
from models.livro import Livro
from models.prateleira import Prateleira

entrada_livro_bp = Blueprint(
    "entrada_livro",
    __name__
)


@entrada_livro_bp.route("/entrada_livro", methods=["GET", "POST"])
@login_required

def entrada_livro():

    message = ""

    if request.method == "POST":

        titulo = request.form.get("titulo")
        autor = request.form.get("autor")
        preco = request.form.get("preco")
        tema = request.form.get("tema")
        quantidade = request.form.get("quantidade")
        id_prateleira = request.form.get("id_prateleira")

        if not titulo:
            message = "Título obrigatório"

        elif not autor:
            message = "Autor obrigatório"

        elif not preco:
            message = "Preço obrigatório"

        elif not tema:
            message = "Tema obrigatório"

        elif not quantidade:
            message = "Quantidade obrigatória"

        elif not id_prateleira:
            message = "Prateleira obrigatória"            

        else:

            livro = Livro(
                titulo=titulo,
                autor=autor,
                preco_compra=float(preco),
                quantidade=int(quantidade),
                id_prateleira=int(id_prateleira),
                tema=tema
            )

            db.session.add(livro)
            db.session.commit()

            message = "Livro cadastrado com sucesso"

    prateleiras = Prateleira.query.all()

    return render_template(
        "estoque/entrada_livro.html",
        prateleiras=prateleiras,
        message=message
    )
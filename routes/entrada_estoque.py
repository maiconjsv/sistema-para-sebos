from flask import Blueprint, request, render_template

from database import db
from models.livro import Livro
from models.prateleira import Prateleira

entrada_estoque_bp = Blueprint(
    "entrada_estoque",
    __name__
)


@entrada_estoque_bp.route("/", methods=["GET", "POST"])
def entrada_estoque():

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
        "entrada_estoque.html",
        prateleiras=prateleiras,
        message=message
    )
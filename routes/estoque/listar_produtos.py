from flask import Blueprint, request, render_template
from auth import login_required
from models.livro import Livro

listar_produtos_bp = Blueprint("livros", __name__)

@listar_produtos_bp.route("/livros")
@login_required
def listar_livros():

    busca = request.args.get("busca")
    tipo_busca = request.args.get("tipo_busca", "titulo")

    query = Livro.query

    if busca:

        if tipo_busca == "titulo":

            query = query.filter(
                Livro.titulo.ilike(f"%{busca}%")
            )

        elif tipo_busca == "autor":

            query = query.filter(
                Livro.autor.ilike(f"%{busca}%")
            )

        elif tipo_busca == "preco":

            try:

                preco = float(busca)

                query = query.filter(
                    Livro.preco_compra == preco
                )

            except ValueError:

                pass

    page = request.args.get("page", 1, type=int)

    livros = query.paginate(
        page=page,
        per_page=9
    )

    return render_template(
        "estoque/listar.html",
        livros=livros,
        busca=busca,
        tipo_busca=tipo_busca
    )
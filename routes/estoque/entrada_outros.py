from auth import login_required
from models.classificacoes import Classificacao
from models.setor import Setor
from flask import Blueprint, render_template, g, session
from routes.usuario import login


entrada_outros_bp = Blueprint("entrada_outros", __name__)

@entrada_outros_bp.route("/entrada_outros", methods=["GET", "POST"])

@login_required

def entrada_outros():

    setores = Setor.query.filter_by(ativo=True).all()
    classificacoes = Classificacao.query.all()

    return render_template(
        "estoque/entrada_outros.html",
        setores=setores,
        classificacoes=classificacoes,
        usuario_logado = session["usuario_nome"]
    )
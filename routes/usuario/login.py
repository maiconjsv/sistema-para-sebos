from flask import Blueprint, request, render_template, redirect, session, flash
from models.usuario import Usuario
from database import db
from werkzeug.security import check_password_hash
import os


login_bp = Blueprint(
    "login",
    __name__
)

@login_bp.route("/", methods=["GET", "POST"])

def login():

    if request.method == "POST":

        message = ''
        email = request.form.get("login")
        senha = request.form.get("senha")

        usuario = Usuario.query.filter_by(
            login=email
        ).first()

        if usuario:

            senha_correta = check_password_hash(
                usuario.senha,
                senha
            )

            if senha_correta:

                session["usuario_id"] = usuario.id
                session["usuario_nome"] = usuario.nome

                return redirect("/entrada_livro")

        flash("Login ou senha inválidos")
        usuario_logado = session["usuario_nome"]
    return render_template(
        "usuario/login.html",
        versao_sistema="1.0.0",
    )
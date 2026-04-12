from flask import Blueprint, session, Request
from models.usuario import Usuario
from database import db


def usuario_logado():
    usuario = Usuario.query.filter_by(
    ).first()
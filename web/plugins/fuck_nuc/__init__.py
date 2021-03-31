from sanic import Blueprint

api = Blueprint('login','/login')

from .login import *

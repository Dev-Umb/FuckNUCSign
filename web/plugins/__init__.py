from sanic import Blueprint

from .fuck_nuc import api

content = Blueprint.group(api, url_prefix='/v1')

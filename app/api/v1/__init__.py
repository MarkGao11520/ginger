"""
create by gaowenfeng on 
"""

from flask import Blueprint
from app.api.v1 import book, user, client

__author__ = "gaowenfeng"


def create_blueprint_v1():
    bp_v1 = Blueprint('v1', __name__)

    book.api.register(bp_v1)
    user.api.register(bp_v1)
    client.api.register(bp_v1)
    return bp_v1

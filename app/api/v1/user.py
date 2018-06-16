"""
create by gaowenfeng on 
"""

from app.libs.redprint import Redprint
from app.libs.token_auth import auth
from flask import jsonify

from app.models.user import User

__author__ = "gaowenfeng"

api = Redprint('user')


@api.route('/<int:uid>', methods=['GET'])
@auth.login_required
def get_user(uid):
    user = User.query.get_or_404(uid)
    return jsonify(user), 200

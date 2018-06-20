"""
create by gaowenfeng on 
"""
from app import create_app
from app.models.base import db
from app.models.user import User

__author__ = "gaowenfeng"

app = create_app()
with app.app_context():
    with db.auto_commit():
        user = User()
        user.nickname = 'super'
        user.password = '123456'
        user.email = '999@qq.com'
        user.auth = 2
        db.session.add(user)

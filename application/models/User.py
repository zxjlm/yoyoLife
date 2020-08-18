"""
@author: harumonia
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: zxjlm233@gmail.com
@software: Pycharm
@file: User.py
@time: 2020/8/15 20:17
@desc:
"""
from application.extensions import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model, UserMixin):
    __tablename__ = 'tb_user'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, comment='id')
    username = db.Column(db.String(20), comment='用户名')
    password = db.Column(db.String(128), comment='密码')
    locale = db.Column(db.String(20))
    last_login = db.Column(db.DateTime, comment='最后登录日期')
    last_ip = db.Column(db.String(16), comment='最后登录日期')

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def validate_password(self, password):
        return check_password_hash(self.password, password)

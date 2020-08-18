"""
@author: harumonia
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: zxjlm233@gmail.com
@software: Pycharm
@file: Todos.py
@time: 2020/8/15 20:17
@desc:
"""
from application.extensions import db


class Todos(db.Model):
    __tablename__ = 'tb_todolist'

    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    body = db.Column(db.Text, nullable=False, comment='内容')
    date = db.Column(db.Date, comment='日期')
    done = db.Column(db.Boolean, comment='状态', default=False)
    author_id = db.Column(db.ForeignKey('tb_user.id', ondelete='CASCADE', onupdate='CASCADE'), index=True,
                          comment='关联对象')
    author = db.relationship('User', primaryjoin='Todos.author_id == User.id', backref='todos')

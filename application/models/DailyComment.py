"""
@author: harumonia
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: zxjlm233@gmail.com
@software: Pycharm
@file: DailyComment.py
@time: 2020/8/15 20:17
@desc:
"""
from application.extensions import db


class DailyComment(db.Model):
    __tablename__ = 'tb_daily_comment'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, comment='id')
    body = db.Column(db.Text, nullable=False, comment='内容')
    date = db.Column(db.Date)
    author_id = db.Column(db.ForeignKey('tb_user.id', ondelete='CASCADE', onupdate='CASCADE'), index=True,
                          comment='关联对象')
    author = db.relationship('User', primaryjoin='DailyComment.author_id == User.id', backref='dailycomments')

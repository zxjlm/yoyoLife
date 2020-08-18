"""
@author: harumonia
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: zxjlm233@gmail.com
@software: Pycharm
@file: GithubTendency.py
@time: 2020/8/15 20:17
@desc:
"""
from application.extensions import db


class GithubTendency(db.Model):
    __tablename__ = 'tb_github'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, comment='id')
    date = db.Column(db.Date, comment='日期')
    url = db.Column(db.String(150), comment='链接')
    description = db.Column(db.String(255), comment='简介')
    language = db.Column(db.String(100), comment='语言')
    stars = db.Column(db.Integer, comment='星')
    forks = db.Column(db.Integer)
    currentPeriodStars = db.Column(db.Integer, comment='最近的星')

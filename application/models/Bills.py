"""
@author: harumonia
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: zxjlm233@gmail.com
@software: Pycharm
@file: Bills.py
@time: 2020/8/15 20:16
@desc:
"""
from application.extensions import db


class ConsumptionTypeDict(db.Model):
    __tablename__ = 'tb_consumption_type_dict'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    consumption_type = db.Column(db.String(100))
    mark = db.Column(db.String(255))


class Bills(db.Model):
    __tablename__ = 'tb_bill'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    payfor = db.Column(db.String(255), comment='消费对象')
    money = db.Column(db.Float, comment='消费金额')
    author_id = db.Column(db.ForeignKey('tb_user.id', ondelete='CASCADE', onupdate='CASCADE'), index=True,
                          comment='关联对象')

    consumption_type_id = db.Column(
        db.ForeignKey('tb_consumption_type_dict.id', ondelete='CASCADE', onupdate='CASCADE'),
        index=True, comment='关联消费类型字典表')
    status = db.Column(db.String(1), comment='状态')
    datetime = db.Column(db.DateTime, comment='日期时间')
    mark = db.Column(db.String(255))
    author = db.relationship('User', primaryjoin='Bills.author_id == User.id', backref='bills')
    consumption_type = db.relationship('ConsumptionTypeDict',
                                       primaryjoin='Bills.consumption_type_id == ConsumptionTypeDict.id',
                                       backref='bills')

    def to_json(self):
        return {
            'id': self.id,
            'payfor': self.payfor,
            'money': self.money,
            'author': self.author_id,
            'status': self.status,
            'mark': self.mark,
            'consumption_type': self.consumption_type.consumption_type,
            'datetime': self.datetime
        }

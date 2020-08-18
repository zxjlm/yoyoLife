"""
@author: harumonia
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: zxjlm233@gmail.com
@software: Pycharm
@file: __init__.py
@time: 2020/7/26 23:52
@desc:
"""
from application.blueprints.auth import auth_bp
from application.blueprints.bill import bill_bp
from application.blueprints.home import home_bp
from application.blueprints.todo import todo_bp

all_bp = [
    auth_bp,
    bill_bp,
    home_bp,
    todo_bp
]
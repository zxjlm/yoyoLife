# -*- coding: utf-8 -*-
"""
    :author: Harumonia
    :url: http://harumonia.top
    :copyright: © 2020 harumonia<zxjlm233@gmail.com>
    :license: MIT, see LICENSE for more details.
"""
from faker import Faker
from flask import render_template, redirect, url_for, Blueprint, request, jsonify
from flask_babel import _
from flask_login import login_user, logout_user, login_required, current_user

from application.extensions import db
from application.form import LoginForm
from application.models.User import User
from application.models.Bills import Bills
from application.models.Todos import Todos

auth_bp = Blueprint('auth', __name__)
fake = Faker()


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    emsg = None
    if form.validate_on_submit():
        user_name = form.username.data
        password = form.password.data
        user = User.query.filter_by(username=user_name).first()
        if user is None:
            emsg = "用户名或密码密码有误"
        else:
            if user.validate_password(password):  # 校验密码
                login_user(user)  # 创建用户 Session
                return redirect(request.args.get('next') or url_for('home.index'))
            else:
                emsg = "用户名或密码密码有误"
    return render_template('_login.html', form=form, emsg=emsg)


@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    # return jsonify(message=_('Logout success.'))
    return redirect(url_for('home.index'))


@auth_bp.route('/register')
def register():
    # iyates other
    # generate a random account for demo use
    username = fake.user_name()
    # make sure the generated username was not in database
    while User.query.filter_by(username=username).first() is not None:
        username = fake.user_name()
    password = fake.word()
    user = User(username=username)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()

    todo = Todos(body=_('看书半小时'), done=False, author=user)
    todo2 = Todos(body=_('完成一道算法题'), done=False, author=user)
    todo3 = Todos(body=_('正念|反思'), done=False, author=user)
    todo4 = Todos(body=_('吃水果'), done=True, author=user)
    bill = Bills(payfor="吃饭", money=15, author=user)
    bill2 = Bills(payfor="交通", money=4.5, author=user)
    db.session.add_all([todo, todo2, todo3, todo4, bill, bill2])
    db.session.commit()

    return jsonify(username=username, password=password, message=_('Generate success.'))

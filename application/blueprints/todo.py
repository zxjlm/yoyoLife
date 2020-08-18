# -*- coding: utf-8 -*-
"""
    :author: Harumonia
    :url: http://harumonia.top
    :copyright: © 2020 harumonia<zxjlm233@gmail.com>
    :license: MIT, see LICENSE for more details.
"""
import time

from flask import render_template, request, Blueprint, jsonify
from flask_babel import _
from flask_login import current_user, login_required

from application.extensions import db
from application.models.Todos import Todos

todo_bp = Blueprint('todo', __name__, url_prefix='/todo')


@todo_bp.route('/')
@login_required
def init():
    todos = Todos.query.filter(Todos.author_id == current_user.id,
                               Todos.date.between(time.strftime('%Y-%m-%d 00:00:00'),
                                                  time.strftime('%Y-%m-%d 23:59:59'))).all()
    if len(todos) != 0:
        flag = True
    else:
        flag = False
    return render_template('todo.html', todos=todos,flag=flag)


@todo_bp.route('/items/new', methods=['POST'])
@login_required
def new_item():
    data = request.get_json()
    if data is None or data['body'].strip() == '':
        return jsonify(message=_('Invalid item body.')), 400
    item = Todos(body=data['body'], author=current_user._get_current_object(), date=time.strftime('%Y-%m-%d %H:%M:%S'))
    db.session.add(item)
    db.session.commit()
    return jsonify(html=render_template('_item.html', todo=item), message='+1')


@todo_bp.route('/item/edit', methods=['POST'])
@login_required
def edit_item():
    data = request.get_json()
    item = Todos.query.get_or_404(data['id'])
    if current_user != item.author:
        return jsonify(message=_('Permission denied.')), 403

    if data is None or data['body'].strip() == '':
        return jsonify(message=_('Invalid item body.')), 400
    item.body = data['body']
    db.session.commit()
    return jsonify(message=_('Todo updated.'))


@todo_bp.route('/item/toggle/<string:item_id>', methods=['GET'])
@login_required
def toggle_item(item_id):
    item = Todos.query.get_or_404(int(item_id))
    if current_user != item.author:
        return jsonify(message=_('Permission denied.')), 403

    item.done = not item.done
    db.session.add(item)
    db.session.commit()
    return jsonify(message=_('Todo toggled.'), status=item.done)


@todo_bp.route('/item/delete/<string:item_id>', methods=['DELETE'])
@login_required
def delete_item(item_id):
    item = Todos.query.get_or_404(item_id)
    if current_user != item.author:
        return jsonify(message=_('Permission denied.')), 403

    db.session.delete(item)
    db.session.commit()
    return jsonify(message=_('Todo deleted.'))


@todo_bp.route('/item/clear', methods=['DELETE'])
@login_required
def clear_items():
    items = Todos.query.with_parent(current_user).filter_by(done=True).all()
    for item in items:
        db.session.delete(item)
    db.session.commit()
    return jsonify(message=_('All clear!'))

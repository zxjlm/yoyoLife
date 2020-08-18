# -*- coding: utf-8 -*-
"""
    :author: Harumonia
    :url: http://harumonia.top
    :copyright: © 2020 harumonia<zxjlm233@gmail.com>
    :license: MIT, see LICENSE for more details.
"""
from flask import render_template, Blueprint, current_app, make_response, jsonify
# from flask_babel import _
from flask_login import current_user, login_required

from application.extensions import db

home_bp = Blueprint('home', __name__)


@home_bp.route('/')
@login_required
def index():
    # return 'success'
    return render_template('index.html')


@home_bp.route('/intro')
def intro():
    return render_template('base.html')


@home_bp.route('/set-locale/<locale>')
def set_locale(locale):
    if locale not in current_app.config['TODOISM_LOCALES']:
        return jsonify(message=_('Invalid locale.')), 404

    response = make_response(jsonify(message=_('Setting updated.')))
    if current_user.is_authenticated:
        current_user.locale = locale
        db.session.commit()
    else:
        response.set_cookie('locale', locale, max_age=60 * 60 * 24 * 30)
    return response

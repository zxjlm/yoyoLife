# -*- coding: utf-8 -*-
"""
    :author: Harumonia
    :url: http://harumonia.top
    :copyright: © 2020 harumonia<zxjlm233@gmail.com>
    :license: MIT, see LICENSE for more details.
"""
import os

from flask import Flask
# from flask_babel import _
from application.blueprints import all_bp
from application.extensions import db, login_manager, babel, migrate
import application.models
from application.settings import config


def create_app(config_name=None):
    if config_name is None:
        config_name = os.getenv('FLASK_CONFIG', 'development')

    app = Flask('application')
    app.config.from_object(config[config_name])

    register_extensions(app)
    register_blueprints(app)
    # register_commands(app)
    # register_errors(app)
    # register_template_context(app)
    return app


def register_extensions(app):
    db.init_app(app)
    login_manager.init_app(app)
    babel.init_app(app)
    migrate.init_app(app, db)


def register_blueprints(app):
    for bp in all_bp:
        app.register_blueprint(bp)


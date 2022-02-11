import flask
import flask_bootstrap

from config import config

bootstrap = flask_bootstrap.Bootstrap()


def create_app(config_name='default'):
    app = flask.Flask('oliver')
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(app)

    @app.route("/welcome")
    def welcome():
        return "Welcome to Oliver"

    from .bot import bot as bot_blueprint
    app.register_blueprint(bot_blueprint, url_prefix='/bot/v1')

    return app

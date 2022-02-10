import flask


from config import config


def create_app(config_name='default'):
    app = flask.Flask('oliver')
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    @app.route("/welcome")
    def welcome():
        return "Welcome to Oliver"
        
    return app

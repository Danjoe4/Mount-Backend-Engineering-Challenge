from flask import Flask

def init_app():
    """Initialize the core application."""
    # logging
    #import logging
    #logging.basicConfig(filename='debug_log.log', level=logging.DEBUG)

    app = Flask(__name__)
    # load the configuration values from a dict with env variables
    # app.config.from_object("config.DevConfig")

    #logging.debug(app.config)

    with app.app_context():

        # Import parts of our application
        from .main.api.item import item_bp
        app.register_blueprint(item_bp, url_prefix='/item')
        from .main.api.root import root_bp
        app.register_blueprint(root_bp, url_prefix='/')


        return app
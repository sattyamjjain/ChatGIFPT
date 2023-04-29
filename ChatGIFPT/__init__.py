from flask import Flask
from flask_bcrypt import Bcrypt

flask_bcrypt = Bcrypt()


def create_app():
    app = Flask(__name__)
    flask_bcrypt.init_app(app)

    @app.shell_context_processor
    def ctx():
        return {"app": app}

    return app

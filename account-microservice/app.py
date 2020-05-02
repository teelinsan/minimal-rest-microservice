import os
import connexion
from flask_injector import FlaskInjector
from connexion.resolver import RestyResolver
from providers.MongoProvider import MongoProvider
from injector import Binder
from flask_cors import CORS


def configure(binder: Binder) -> Binder:
    binder.bind(
        MongoProvider
    )


if __name__ == '__main__':
    app = connexion.App(__name__, specification_dir='swagger/')  # Provide the app and the directory of the docs
    CORS(app.app)
    app.add_api('accounts-service-docs.yaml', resolver=RestyResolver('api'))
    FlaskInjector(app=app.app, modules=[configure])
    app.run(port=int(os.environ.get('PORT', 2020)))  # os.environ is handy if you intend to launch on heroku

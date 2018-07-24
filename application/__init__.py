from flask import Flask
from flask_restplus import Api
from instance.config import configuration


def create_app(config):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(configuration[config])
    app.url_map.strict_slashes = False

    
    # initialize api
    api = Api(app=app,
              title='My diary',
              doc='/api/v1/documentation',
              description='My Diary is an online journal where users can pen down their thoughts and feelings')
    doc = ('/api/v1/documentation')


    from application.views.views import api as entries
    api.add_namespace(entries, path='/api/v1')

    return app

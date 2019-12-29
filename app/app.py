from flask import Flask
from views.index import index_blueprint

application = Flask(__name__)
application.register_blueprint(index_blueprint)


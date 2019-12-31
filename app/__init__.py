from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login'

from app import routes, models


#db = SQLAlchemy()
#login = LoginManager()
#migrate = Migrate()
#login.login_view = 'auth.login'
#login.login_message = _l('Please log in to access this page.')
#mail = Mail()
#bootstrap = Bootstrap()
#moment = Moment()
#babel = Babel()

#def create_app(config_class=Config):
#    app = Flask(__name__)
#    app.config.from_object(config_class)
#
#    db.init_app(app)
#    migrate.init_app(app)
#    login.init_app(app)
#    mail.init_app(app)
#    bootstrap.init_app(app)
#    moment.init_app(app)
#    babel.init_app(app)


#    if not app.debug and not app.testing:


#    return app

#from app.errors import bp as errors_bp
#app.register_blueprint(errors_bp)


#from app import routes, models
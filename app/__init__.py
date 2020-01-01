import os
import logging

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

from logging.handlers import RotatingFileHandler
from logging.handlers import SMTPHandler
from app import routes, models, errors


if not app.debug:
    if app.config['MAIL_SERVER']:
        auth = None
        if app.config['MAIL_USERNAME'] or app.config['MAIL_PASSWORD']:
            auth = (app.config['MAIL_USERNAME'], app.config['MAIL_PASSWORD'])
        secure = None
        if app.config['MAIL_USE_TLS']:
            secure = ()
        mail_handler = SMTPHandler(
            mailhost=(app.config['MAIL_SERVER'], app.config['MAIL_PORT']),
            fromaddr='no-reply@' + app.config['MAIL_SERVER'],
            toaddrs=app.config['ADMINS'], subject='Masjid Member List Failure',
            credentials=auth, secure=secure)
        mail_handler.setLevel(logging.ERROR)
        app.logger.addHandler(mail_handler)

    if not os.path.exists('logs'):
        os.mkdir('logs')
    file_handler = RotatingFileHandler('logs/masjidpy.log', maxBytes=10240,
                                       backupCount=10)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)

    app.logger.setLevel(logging.INFO)
    app.logger.info('Masjid Member List startup')


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


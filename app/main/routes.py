from werkzeug.urls import url_parse
from flask import render_template, flash, redirect, url_for, request, g, current_app

from flask_login import current_user, login_user, logout_user, login_required
from flask_babel import lazy_gettext as _l, get_locale

from app import db
from app.models import User
from app.main import bp

@bp.before_request
def before_request():
    # ...
    g.locale = str(get_locale())

@bp.route('/')
@bp.route('/index')
@login_required
def index():
    user = {'username': 'Doods'}

    members = [
        {
            'name': 'Mahmudul Hoque',
            'address': {
                'street': "22 Carlton Close",
                'city': 'Luton',
                'postcode': 'LU3 1ER'
            },
            'mobile': '07961 103217',
            'email': 'm.hoque@gmail.com'
        },
        {
            'name': 'Ubaid Hoque',
            'address': {
                'street': "22 Carlton Close",
                'city': 'Luton',
                'postcode': 'LU3 1ER'
            },
            'mobile': '07961 1111111',
            'email': 'u.hoque@gmail.com'
        }
    ]    
    return render_template('index.html', title=_l('Home'), members=members)

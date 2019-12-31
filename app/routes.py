from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
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

    return render_template('index.html', title='Home', user=user, members=members)
from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm

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

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)
from flask import Blueprint, render_template 
from flask_login import login_required, current_user
from .backend import get_and_clean_data , exampleoutput

main = Blueprint('main', __name__)
dataframe = get_and_clean_data()
dataexample = exampleoutput(dataframe)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/test')
def test():
    return render_template('test.html',data=dataexample)

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)
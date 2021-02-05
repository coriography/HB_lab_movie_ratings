"""Server for movie ratings app."""

from flask import (Flask, render_template, request, flash, session, redirect)

from model import connect_to_db
import crud

from jinja2 import StrictUndefined

print(f"we in the serverrr {__name__}")

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined

@app.route('/')
def homepage():
    return render_template('homepage.html')

@app.route('/', methods=['POST'])
def log_in():
    """submits a log in form"""
    
    form_email = request.form.get('login_email')
    form_password = request.form.get('login_password')

    user = crud.get_user_by_email(form_email)

    if user.password == form_password:
        session['user_id'] = user.user_id
        flash(f'logged in user {form_email}')
        
    else:
        flash(f'incorrect password :sad face:')

    return redirect('/')

@app.route('/movies')
def all_movies():
    """View all movies."""
    # import pdb; pdb.set_trace()
    movies = crud.get_movies()

    return render_template('all_movies.html', movies=movies)

@app.route('/movies/<movie_id>')
def show_movie(movie_id):
    """View movie details."""

    movie = crud.get_movie_by_id(movie_id)

    return render_template('movie_details.html', movie=movie)

@app.route('/users')
def all_user():
    """view all users"""
    users = crud.get_users()

    return render_template('all_users.html', users=users)


@app.route('/users', methods=['POST'])
def register_user():

    form_email = request.form.get('email')
    form_password = request.form.get('password')
    user = crud.get_user_by_email(form_email)

    if user == None:
        crud.create_user(form_email, form_password)
        flash(f"user {form_email} has been created!")
    
    else: 
        flash(f"user {form_email} already exists")

    return redirect('/')


@app.route('/users/<user_id>')
def show_user(user_id):
    """view user details"""

    user = crud.get_user_by_id(user_id)

    return render_template('user_details.html', user=user)


if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)

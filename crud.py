from model import db, User, Movie, Rating, connect_to_db

print(f"howdyyy {__name__}")

def create_user(email, password):
    """create and return a new user"""

    user = User(email=email, password=password)
    
    db.session.add(user)
    db.session.commit()

    return user

def create_movie(title, overview, release_date, poster_path):
    """create and return a new movie."""

    movie = Movie(title=title, overview=overview, release_date=release_date, poster_path=poster_path)

    db.session.add(movie)
    db.session.commit()

    return movie


def get_movies():
    """returns all movies."""

    return Movie.query.all()


def get_movie_by_id(movie_id):
    """returns movie details"""

    movie = Movie.query.get(movie_id)

    return movie


def create_rating(user, movie, score):
    """create and return a new rating."""

    rating = Rating(user=user, movie=movie, score=score)

    db.session.add(rating)
    db.session.commit()

    return rating


def get_users():
    """returns all users"""
    users = User.query.all()

    return users

def get_user_by_id(user_id):
    """gets user by id"""

    user = User.query.get(user_id)

    return user

def get_user_by_email(email):

    return User.query.filter(User.email == email).first()


if __name__ == '__main__':
    from server import app
    connect_to_db(app)


from flask import Flask
from flask import url_for

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'
#
#
# @app.route('/')
# def index(): pass
#
#
# @app.route('/login')
# def login(): pass
#
#
# @app.route('/user/<username>')
# def profile(username): pass
#
#
# with app.test_request_context():
#     print(url_for('index'))
#     print(url_for('login'))
#     print(url_for('login', next='/'))
#     print(url_for('profile', username='John Doe'))




# @app.route('/')
# def index():
#     return 'Index Page'
#
#
# @app.route('/hello')
# def hello():
#     return 'Hello, World'
#
#
# @app.route('/Cabana/')
# def projects():
#     return 'The project page'
#
#
# @app.route('/about')
# def about():
#     return 'The about page'

if __name__ == "__main__":
    app.run()

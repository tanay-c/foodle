from flask import Flask, url_for, render_template, request
# escape helps against injection attacks
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods = ['GET', 'POST'])
def login():
    # show the user profile for that user
    if request.method == 'POST':
        return 'login'
    else:
        return 'show_login_page'

@app.route('/user/<username>')
def profile(username):
    # show the user profile for that user
    return f'User {escape(username)}'

if (__name__ == '__main__'):
    app.run(debug=True)

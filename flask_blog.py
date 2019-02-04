from flask import Flask, render_template, url_for
#from python_secrets import secrets
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

#app.config['KEY'] = secrets.generate_token_hex(12)

posts = [{'author': 'James',
         'title': 'blogpost1',
         'content': 'hello all! Good to see you!',
         'date': 'January 22, 2019'},
        {'author': 'Steve',
         'title': 'blogpost2',
         'content': 'It was really nice to meet you all',
         'date': 'January 21, 2019'}
        ]

@app.route("/")
@app.route("/home")
@app.route("/index")
def home():
    return render_template('home.html', posts=posts)

@app.route("/name")
def name():
    return "<h1>Blaise</h1>"

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)

@app.route("/login")
def login():
    login = LoginForm()
    return render_template('login.html', title='Login', form=login)

if __name__ == '__name__':
    app.run(debug=True)
from flask import Flask , render_template 
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/login')
def index():
    return render_template('index.html')


@app.route('/login/user')
def home():
    return render_template('home.html')


@app.route('/login/user/graphics')
def graphics():
    return render_template('graphics.html')



@app.route('/login/user/camera')
def camera():
    return render_template('camera.html')


@app.route('/signup')
def signup():
    return render_template('signup.html')



@app.route('/login/user/graphics2')
def graphics2():
    return render_template('graphics2.html')
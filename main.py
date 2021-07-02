from flask import Flask , render_template , request
from flask_bootstrap import Bootstrap
from werkzeug.utils import redirect
from  service.controller_users import insertar_usuario
from service.database import obtener_conexion


app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/login')
def index():
    return render_template('index.html')

@app.route('/log_user' , methods=["POST"])
def log_user():
    email = request.form["email"]
    password = request.form["password"]
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute('SELECT * FROM usuarios WHERE email = %s AND password = %s', (email, password))
        cuenta = cursor.fetchone()
        if cuenta:
            return redirect('/home')
        else:
            return redirect('/login')


@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/home/graphics')
def graphics():
    return render_template('graphics.html')



@app.route('/home/graphics2')
def graphics2():
    return render_template('graphics2.html')


@app.route('/home/camera')
def camera():
    return render_template('camera.html')


@app.route('/signup')
def signup():
    return render_template('signup.html')


@app.route("/save_user" , methods= ["POST"])
def save_user():
    nombre = request.form["Nombre"]
    ap_paterno = request.form["A_Paterno"]
    ap_materno = request.form["A_Materno"]
    email = request.form["email"]
    contraseña = request.form["password"]
    insertar_usuario(nombre , ap_paterno , ap_materno , email , contraseña)
    return redirect("/home")

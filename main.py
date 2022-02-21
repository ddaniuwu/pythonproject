from flask import Flask , render_template , request
from flask_bootstrap import Bootstrap
from werkzeug.utils import redirect
from  service.controller_users import insertar_usuario
from service.database import obtener_conexion
import cv2

#from detectando import capturar

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/login')
def index():
    return render_template('index.html')



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

@app.route('/recog')
def recognize():
    cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
    objeto = cv2.CascadeClassifier('cascade.xml')
    while True:
        ret,frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        obj = objeto.detectMultiScale(gray,
        scaleFactor = 5,
        minNeighbors = 91,
        minSize=(70,78))
        
        for (x,y,w,h) in obj:
            cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
            cv2.putText(frame,'Detectando...',(x,y-10),2,0.7,(0,255,0),2,cv2.LINE_AA)
                
            cv2.imshow('frame',frame)
            
            if cv2.waitKey(1) == 27:
                    break
                
            cap.release()
            cv2.destroyAllWindows()

@app.route('/about')
def about():
 return render_template('about.html')



@app.route('/tools')
def tools():
 return render_template('tools.html')
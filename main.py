from flask import Flask,render_template,request,flash,g
from forms import UserForm
from flask_wtf.csrf import CSRFProtect
from config import DevelopmentConfig

from models import db
from models import Alumnos

app=Flask(__name__)
app.config.from_object(DevelopmentConfig)
csrf = CSRFProtect()

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"),404

@app.route("/",methods=['GET','POST'])
def index():
    formulario = UserForm(request.form)
    if request.method == 'POST':
        alumno = Alumnos(nombre = formulario.nombre.data, 
                         apaterno = formulario.apaterno.data,
                         amaterno = formulario.amaterno.data,
                         email = formulario.email.data)
        db.session.add(alumno)
        db.session.commit()
        print("Finalizó")
    return render_template("index.html", form=formulario)

@app.route("/alumnos",methods=["GET","POST"])
def alumnos():
    alumno_clase = UserForm(request.form)
    nombre = ""
    apaterno = ""
    amaterno = ""
    edad = ""
    email = ""
    mensaje = ""
    if request.method == "POST" and alumno_clase.validate():
        nombre = alumno_clase.nombre.data
        apaterno = alumno_clase.apaterno.data
        amaterno = alumno_clase.amaterno.data
        edad = alumno_clase.edad.data
        email = alumno_clase.email.data

        mensaje = "Bienvenido, {}".format(nombre + " " + amaterno)
        flash(mensaje)
    return render_template("alumnos.html",form=alumno_clase,nombre=nombre,apaterno=apaterno,amaterno=amaterno,edad=edad,email=email)

@app.route("/ABC_Completo", methods=[ "GET", "POST"])
def ABCompleto():
    alumno = Alumnos.query.all()
    return render_template("ABC_Completo.html", alumnos=alumno)

if __name__ == "__main__":
    csrf.init_app(app)
    db.init_app(app)

    with app.app_context():
        db.create_all()
    app.run()
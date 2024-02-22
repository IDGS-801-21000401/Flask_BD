from wtforms import validators,Form,StringField,IntegerField,EmailField

class UserForm(Form):
    nombre = StringField("nombre",[
        validators.DataRequired(message='El campo es requerido.'),
        validators.length(min=4,max=10,message='El minimo es 4 y el máximo es 10'),
    ])
    apaterno = StringField("apaterno",[
        validators.DataRequired(message='El campo es requerido.'),
        validators.length(min=4,max=10,message='El minimo es 4 y el máximo es 10')
    ])
    amaterno = StringField("amaterno",[
        validators.DataRequired(message='El campo es requerido.'),
        validators.length(min=4,max=10,message='El minimo es 4 y el máximo es 10')
    ])
    email = EmailField("email",[
        validators.Email(message='Ingrese un email válido!')
    ])
    edad = IntegerField("edad",[
        validators.DataRequired(message='El campo es requerido.'),
    ])
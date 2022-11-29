from flask_wtf import Form
from wtforms import *
from wtforms import validators
from wtforms import ValidationError

class Contactform(Form):

    name=TextField("Student name",[validators.InputRequired("please enter your name")])
    Gender=RadioField("Gender",choices=[('M','male'),('F','female')])
    Address=TextField("address")

    email=TextField("Email",[validators.InputRequired("please enter email")])

    validators.Email("please enter email")
    age=IntegerField("age")
    language=SelectField('programming lang',choices=[('java'),('c++'),('c')])

    submit=SubmitField("submit")
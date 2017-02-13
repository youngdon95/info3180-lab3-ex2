from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import InputRequired,Email,Required
from wtforms.fields import TextField, TextAreaField, SubmitField



class UserForm(FlaskForm):
    name = StringField("Please enter your full name", validators=[InputRequired()])
    email = StringField('Please Enter your email', validators=[InputRequired()])
    subject = StringField('Please enter the subject for your message', validators=[InputRequired()])
    message = TextAreaField('Please Enter your message', validators=[InputRequired()])
   
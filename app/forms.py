from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class NameForm(FlaskForm):
    name= StringField('What is your name?', validators=[DataRequired()])
    rank= StringField('What is your role?', validators=[DataRequired()])
    submitt= SubmitField('Enter Data')

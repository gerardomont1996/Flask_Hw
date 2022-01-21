from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo


class RegisterForm(FlaskForm):
    name=StringField('Name',validators=[DataRequired()])
    phone=StringField('Phone',validators=[DataRequired()])
    address= StringField('Address',validators=[DataRequired()])
    submit= SubmitField('Submit')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')


class EditbookForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    phonenumber = StringField('Phone Number', validators=[DataRequired()])
    address = StringField('Address', validators=[DataRequired()])
    submit = SubmitField('Add Contact')
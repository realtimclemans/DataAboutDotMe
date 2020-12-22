from flask_wtf import Form
from wtfrecaptcha.fields import RecaptchaField
from wtforms import TextField, SubmitField, PasswordField, TextAreaField, StringField, validators

class RegisterForm(Form):   
    email_address = StringField('Your email address', [validators.DataRequired(), validators.Length(min=6, max=35)])
    recaptcha = RecaptchaField()


class SigninForm(Form):   
    email_address = StringField('Email address', [validators.DataRequired(), validators.Length(min=6, max=35)])
    password = StringField('Password', [validators.DataRequired(), validators.Length(min=6, max=35)])
    
    recaptcha = RecaptchaField()
    submit = SubmitField('Verify my email address')
from flask_wtf import Form, RecaptchaField
from wtforms import TextField, SubmitField, PasswordField, TextAreaField, StringField, validators

class SignupForm(Form):   
    email_address = PasswordField('Your email address')
    recaptcha = RecaptchaField()
    
    submit = SubmitField('Verify my email address')

class SigninForm(Form):   
    email_address = StringField('Email address', [validators.DataRequired(), validators.Length(min=6, max=35)])
    password = StringField('Password', [validators.DataRequired(), validators.Length(min=6, max=35)])
    
    recaptcha = RecaptchaField()
    submit = SubmitField('Sign in')
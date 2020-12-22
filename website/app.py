import requests
import os
from flask import Flask, request, jsonify, render_template, request, send_from_directory
from form import SigninForm
import random
import string

app = Flask(__name__, static_url_path='', static_folder='static')


SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY
app.config['RECAPTCHA_USE_SSL'] = True
app.config['RECAPTCHA_PUBLIC_KEY'] = os.getenv('RECAPTCHA_PUBLIC_KEY')
RECAPTCHA_PUBLIC_KEY = app.config['RECAPTCHA_PUBLIC_KEY']
app.config['RECAPTCHA_PRIVATE_KEY'] = os.getenv('RECAPTCHA_PRIVATE_KEY')
RECAPTCHA_PRIVATE_KEY = app.config['RECAPTCHA_PRIVATE_KEY']
app.config['RECAPTCHA_OPTIONS']= {'theme':'black'}


def create_verification_token():
    letters = string.ascii_lowercase
    return ''.join([random.choice(letters) for i in range(200)])

def send_verification_email(email_address, verification_token):
    return requests.post(
		"https://api.mailgun.net/v3/%s/messages" % (os.getenv('API_EMAIL_DOMAIN_NAME')),
		auth=("api", "%s" % (os.getenv('MAILGUN_API_KEY'))),
		data={"from": "DataAbout.me email verification <no-reply@%s>" % (os.getenv('API_EMAIL_DOMAIN_NAME')),
			"to": ["%s" % (email_address)],
			"subject": "Verify your email address",
			"text": '<a href="https://%s/verify_email/?token=%s">Verify</a>' % (os.getenv('DOMAIN_NAME'), verification_token)}).text

from wtforms.form import Form
from wtforms import PasswordField
from wtfrecaptcha.fields import RecaptchaField

from wtforms import TextField, SubmitField, PasswordField, TextAreaField, StringField, validators


class CaptchaForm(Form):
    email_address = PasswordField('Your email address', [validators.DataRequired(), validators.Length(min=6, max=35)])
    print('recaptcha pub',RECAPTCHA_PRIVATE_KEY,RECAPTCHA_PUBLIC_KEY)
    captcha = RecaptchaField(public_key=RECAPTCHA_PUBLIC_KEY, private_key=RECAPTCHA_PRIVATE_KEY, secure=True)
    submit = SubmitField('Verify email address')
signup_form = CaptchaForm()
@app.route('/send_email_verification/', methods=['POST'])
def verify_email():
    
    
    signup_form = CaptchaForm(request.form, captcha={'ip_address': request.remote_addr})


    if signup_form.validate():
        verification_token = create_verification_token()
        email_address = request.form.get('email_address')
        sending_response = send_verification_email(email_address, verification_token)
        print('sending response', repr(sending_response))
        if sending_response == 'Forbidden':
            return jsonify({'success': False})
        return jsonify({'success': True}) # regardless if already verified we claim success because we don't disclose to attackers email addresses
    else:
        return jsonify({'success': False, 'is_captcha_valid': False})

@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)

@app.route('/')
def home():

    signin_form = SigninForm()
    return render_template("index.html", signup_form=signup_form)

if __name__ == '__main__':
    app.run(port=5000, debug=True)  
import requests
import os
from flask import Flask, request, jsonify, render_template, request, send_from_directory
from form import SignupForm, SigninForm
import random
import string
import re
import hashlib
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__, static_url_path="", static_folder="static")

SECRET_KEY = os.urandom(32)
app.config["SECRET_KEY"] = SECRET_KEY
app.config["RECAPTCHA_USE_SSL"] = True
app.config["RECAPTCHA_PUBLIC_KEY"] = os.getenv("RECAPTCHA_PUBLIC_KEY")
app.config["RECAPTCHA_PRIVATE_KEY"] = os.getenv("RECAPTCHA_PRIVATE_KEY")
app.config["RECAPTCHA_OPTIONS"] = {"theme": "black"}
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ["DATABASE_URL"]
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
db.app = app
db.init_app(app)
migrate = Migrate(app, db)

from sqlalchemy.dialects.postgresql import UUID, JSON
import uuid



class Customer(db.Model):
    __tablename__ = 'customers'

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True)
    is_suspended = db.Column(db.Boolean(), default=False)
    reason_for_suspension = db.Column(db.String(), nullable=True)
    is_email_address_verified = db.Column(db.Boolean(), default=False)
    verification_token = db.Column(db.String())
    is_identity_verified = db.Column(db.Boolean(), default=False)
    email_address_salt = db.Column(db.String())
    email_address_hash = db.Column(db.String())
    password_salt = db.Column(db.String(), nullable=True)
    password_hash = db.Column(db.String(), nullable=True)
    unique_identifiers = db.Column(JSON, default={}) # example keys: US_state_ID_number, US_state_that_issued_ID, US_social_security_number

    def __init__(self, email_address_salt, email_address_hash, verification_token):
        self.email_address_salt = email_address_salt
        self.email_address_hash = email_address_hash
        self.verification_token = verification_token


def create_random_string():
    letters = string.ascii_lowercase
    return "".join([random.choice(letters) for i in range(200)])


def send_verification_email(email_address, verification_token):
    return requests.post(
        "https://api.mailgun.net/v3/%s/messages" % (os.getenv("API_EMAIL_DOMAIN_NAME")),
        auth=("api", "%s" % (os.getenv("MAILGUN_API_KEY"))),
        data={
            "from": "DataAbout.me email verification <no-reply@%s>"
            % (os.getenv("API_EMAIL_DOMAIN_NAME")),
            "to": ["%s" % (email_address)],
            "subject": "Verify your email address",
            "html": 'Hi! This is a verification email from DataAbout.me If you did not try to sign up please ignore this email.<br/><a href="https://%s/verify_email/?token=%s">Click here to Verify</a> or copy paste https://%s/verify_email/?token=%s into your web browser'
            % (
                os.getenv("DOMAIN_NAME"),
                verification_token,
                os.getenv("DOMAIN_NAME"),
                verification_token,
            ),
        },
    ).text


@app.route("/static/<path:path>")
def send_static(path):
    return send_from_directory("static", path)


@app.route("/", methods=["GET", "POST"])
def home():
    signup_form = SignupForm()
    if request.form:
        if signup_form.validate_on_submit():
            verification_token = create_random_string()
            salt = create_random_string()
            email_address = request.form.get("email_address")
            
            if "+" in email_address:
                return render_template(
                    "index.html",
                    signup_form=signup_form,
                    is_plus_sign_in_email=True,
                    sending_error=False,
                    is_captcha_valid=True,
                    is_email_address_invalid=True
                )
            regex = "^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"
            if not re.search(regex, email_address):
                return render_template(
                    "index.html",
                    signup_form=signup_form,
                    is_plus_sign_in_email=False,
                    is_email_address_invalid=False,
                    sending_error=False,
                    is_captcha_valid=True,
                )
            result = list(db.engine.execute("SELECT '' FROM customers WHERE encode(digest(email_address_salt || ' %s', 'sha1'), 'hex') = email_address_hash" % (email_address)))
            if len(list(result)) > 0: # don't send verification and don't notify attacker that this email belongs to a customer
                return render_template(
                    "index.html",
                    signup_form=signup_form,
                    sending_error=False,
                    sent_verification=True,
                    is_captcha_valid=True,
                    is_email_address_invalid=True
                )
            hash_object = hashlib.sha1()
            hash_object.update(str(salt).encode('utf-8'))
            hash_object.update(str(' ' + email_address).encode('utf-8'))
            email_hash = hash_object.hexdigest()
            customer = Customer(salt, email_hash, verification_token)
            db.session.add(customer)
            db.session.commit()
            sending_response = send_verification_email(
                email_address, verification_token
            )
            if sending_response == "Forbidden":
                return render_template(
                    "index.html",
                    signup_form=signup_form,
                    sending_error=True,
                    is_captcha_valid=True,
                    is_email_address_invalid=True
                )

            return render_template(
                "index.html",
                signup_form=signup_form,
                sending_error=False,
                sent_verification=True,
                is_captcha_valid=True,
                is_email_address_invalid=True
            )  # regardless if already verified we claim success because we don't disclose to attackers email addresses
        else:
            return render_template(
                "index.html", signup_form=signup_form, is_captcha_valid=False, is_email_address_invalid=True
            )
    return render_template("index.html", signup_form=signup_form, is_captcha_valid=True, is_email_address_invalid=True)


if __name__ == "__main__":
    app.run(port=5000, debug=True)

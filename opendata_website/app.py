import requests
import os
from flask import Flask, request, jsonify, render_template, request, send_from_directory
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
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ["OPENDATA_SITE_DATABASE_URL"]
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
db.app = app
db.init_app(app)
migrate = Migrate(app, db)

from sqlalchemy.dialects.postgresql import UUID, JSON
import uuid



class DatasetMetadata(db.Model):
    __tablename__ = 'dataset_metadata'

    table_name = db.Column(db.String(), primary_key=True, unique=True)
    source_url = db.Column(db.String(), nullable=True)
    script_url = db.Column(db.String(), nullable=True)

    def __init__(self, table_name, source_url, script_url):
        self.table_name = table_name
        self.source_url = source_url
        self.script_url = script_url

class WashingtonStateVoter(db.Model):
    __tablename__ = 'washington_state_voters'

    state_voter_id = db.Column(db.String(), primary_key=True, unique=True)
    fname = db.Column(db.String())
    mname = db.Column(db.String())
    lname = db.Column(db.String())
    name_suffix = db.Column(db.String())
    birthdate = db.Column(db.DateTime)
    gender = db.Column(db.String())
    reg_st_num = db.Column(db.String())
    reg_st_frac = db.Column(db.String())
    reg_st_name = db.Column(db.String())
    reg_st_type = db.Column(db.String())
    reg_unit_type = db.Column(db.String())
    reg_st_pre_direction = db.Column(db.String())
    reg_st_post_direction = db.Column(db.String())
    reg_st_unit_num = db.Column(db.String())
    reg_city = db.Column(db.String())
    reg_state = db.Column(db.String())
    reg_zip_code = db.Column(db.String())
    county_code = db.Column(db.String())
    precinct_code = db.Column(db.String())
    precinct_part = db.Column(db.String())
    legislative_district = db.Column(db.String())
    congressional_district = db.Column(db.String())
    mail = db.Column(db.String())
    mail_city = db.Column(db.String())
    mail_zip = db.Column(db.String())
    mail_state = db.Column(db.String())
    mail_country = db.Column(db.String())
    registrationdate = db.Column(db.String())
    absentee_type = db.Column(db.String())
    last_voted = db.Column(db.String())
    status_code = db.Column(db.String())

    def __init__(self, state_voter_id, fname, mname, lname, name_suffix, birthdate, gender, reg_st_num, reg_st_frac, reg_st_name, reg_st_type, reg_unit_type, reg_st_pre_direction, reg_st_post_direction, reg_st_unit_num, reg_city, reg_state, reg_zip_code, county_code, precinct_code, precinct_part, legislative_district, congressional_district, mail, mail_city, mail_zip, mail_state, mail_country, registrationdate, absentee_type, last_voted, status_code):
        state_voter_id = state_voter_id
        fname = fname
        mname = mname
        lname = lname
        name_suffix = name_suffix
        birthdate = birthdate
        gender = gender
        reg_st_num = reg_st_num
        reg_st_frac = reg_st_frac
        reg_st_name = reg_st_name
        reg_st_type = reg_st_type
        reg_unit_type = reg_unit_type
        reg_st_pre_direction = reg_st_pre_direction
        reg_st_post_direction = reg_st_post_direction
        reg_st_unit_num = reg_st_unit_num
        reg_city = reg_city
        reg_state = reg_state
        reg_zip_code = reg_zip_code
        county_code = county_code
        precinct_code = precinct_code
        precinct_part = precinct_part
        legislative_district = legislative_district
        congressional_district = congressional_district
        mail = mail
        mail = mail
        mail = mail
        mail = mail
        mail_city = mail_city
        mail_zip = mail_zip
        mail_state = mail_state
        mail_country = mail_country
        registrationdate = registrationdate
        absentee_type = absentee_type
        last_voted = last_voted
        status_code = status_code    

if __name__ == "__main__":
    app.run(port=6000, debug=True)

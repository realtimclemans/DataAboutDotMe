from app import db
from sqlalchemy.dialects.postgresql import UUID, JSON
import uuid
from flask_sqlalchemy import SQLAlchemy

class Customer(db.Model):
    __tablename__ = 'customers'

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True)
    is_suspended = db.Column(db.Boolean(), default=False)
    is_email_address_verified = db.Column(db.Boolean(), default=False)
    email_address_salt = db.Column(db.String())
    email_address_hash = db.Column(db.String())
    government_identification_numbers = db.Column(JSON, default={}) # example keys: US_state_ID, US_social_security_number

    def __init__(self, url, result_all, result_no_stop_words):
        self.url = url
        self.result_all = result_all
        self.result_no_stop_words = result_no_stop_words

    def __repr__(self):
        return '<id {}>'.format(self.id)
from app import db
from sqlalchemy.dialects.postgresql import UUID, JSON
import uuid
from flask_sqlalchemy import SQLAlchemy

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
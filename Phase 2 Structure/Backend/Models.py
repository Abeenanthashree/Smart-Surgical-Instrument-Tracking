from database import db
from datetime import datetime


class Instrument(db.Model):

    __tablename__ = "instruments"

    id = db.Column(db.Integer, primary_key=True)

    instrument_name = db.Column(db.String(100), nullable=False)

    instrument_type = db.Column(db.String(100))

    rfid_tag = db.Column(db.String(100), unique=True)

    sterilization_status = db.Column(db.String(50))

    operating_theatre = db.Column(db.String(50))

    availability = db.Column(db.String(50))

    last_updated = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    def __repr__(self):
        return f"<Instrument {self.instrument_name}>"

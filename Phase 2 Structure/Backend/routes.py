from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for

from models import Instrument
from database import db

routes = Blueprint("routes", __name__)


@routes.route("/inventory")

def inventory():

    instruments = Instrument.query.all()

    return render_template(
        "inventory.html",
        instruments=instruments
    )


@routes.route("/add", methods=["POST"])

def add_instrument():

    instrument = Instrument(

        instrument_name=request.form["instrument_name"],

        instrument_type=request.form["instrument_type"],

        rfid_tag=request.form["rfid_tag"],

        sterilization_status=request.form["sterilization_status"],

        operating_theatre=request.form["operating_theatre"],

        availability="Available"

    )

    db.session.add(instrument)

    db.session.commit()

    return redirect(url_for("routes.inventory"))

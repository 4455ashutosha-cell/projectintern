from flask import Blueprint
from services.doctor_service import *

doctor_bp = Blueprint(
    "doctors",
    __name__,
    url_prefix="/doctors"
)

@doctor_bp.route("/")
def doctors():

    return get_all_doctors()

@doctor_bp.route("/state/<state>")
def doctor_state(state):

    return get_doctors_by_state(
        state
    )
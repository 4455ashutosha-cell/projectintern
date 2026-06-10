from flask import Blueprint
from services.medicine_service import *

medicine_bp = Blueprint(
    "medicines",
    __name__,
    url_prefix="/medicines"
)

@medicine_bp.route("/")
def medicines():

    return get_all_medicines()

@medicine_bp.route("/search/<name>")
def medicine(name):

    return search_medicine(
        name
    )
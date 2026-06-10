from flask import Blueprint
from services.animal_service import *

animal_bp = Blueprint(
    "animals",
    __name__,
    url_prefix="/animals"
)

@animal_bp.route("/")
def animals():

    return get_all_animals()

@animal_bp.route("/species")
def species():

    return get_species_distribution()
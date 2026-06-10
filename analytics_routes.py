from flask import Blueprint
from services.animal_service import *

analytics_bp = Blueprint(
    "analytics",
    __name__,
    url_prefix="/analytics"
)

@analytics_bp.route("/animal-species")
def animal_species():

    return get_species_distribution()
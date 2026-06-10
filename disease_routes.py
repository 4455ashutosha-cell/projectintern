from flask import Blueprint
from services.disease_service import *

disease_bp = Blueprint(
    "diseases",
    __name__,
    url_prefix="/diseases"
)

@disease_bp.route("/")
def diseases():

    return get_all_diseases()

@disease_bp.route("/symptom/<symptom>")
def symptom(symptom):

    return search_symptoms(
        symptom
    )
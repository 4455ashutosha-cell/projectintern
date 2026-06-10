from flask import Flask
from api.animal_routes import animal_bp
from api.doctor_routes import doctor_bp
from api.disease_routes import disease_bp
from api.medicine_routes import medicine_bp
from api.analytics_routes import analytics_bp

app = Flask(__name__)

app.register_blueprint(animal_bp)
app.register_blueprint(doctor_bp)
app.register_blueprint(disease_bp)
app.register_blueprint(medicine_bp)
app.register_blueprint(analytics_bp)

@app.route("/")
def home():
    return {
        "project": "SmartVet AI",
        "status": "Running"
    }

if __name__ == "__main__":
    app.run(debug=True)
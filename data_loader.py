import pandas as pd

ANIMAL_FILE = "data/Animal_Dairy_Dataset_4200.xlsx"
MEDICINE_FILE = "data/Veterinary_Medicines_Master.xlsx"
DISEASE_FILE = "data/Veterinary_Disease_Warehouse_Project.xlsx"
DOCTOR_FILE = "data/Synthetic_India_Vet_Database_400_Hospitals_4000_Doctors.xlsx"

def load_animals():
    return pd.read_excel(ANIMAL_FILE)

def load_medicines():
    return pd.read_excel(MEDICINE_FILE)

def load_diseases():
    return pd.read_excel(DISEASE_FILE)

def load_doctors():
    return pd.read_excel(DOCTOR_FILE)
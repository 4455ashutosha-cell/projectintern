from database.data_loader import load_diseases

def get_all_diseases():

    df = load_diseases()

    return df.to_dict(
        orient="records"
    )

def search_symptoms(symptom):

    df = load_diseases()

    result = df[
        df["Symptoms"]
        .str.contains(
            symptom,
            case=False,
            na=False
        )
    ]

    return result.to_dict(
        orient="records"
    )
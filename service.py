from database.data_loader import load_animals

def get_all_animals():

    df = load_animals()

    return df.to_dict(
        orient="records"
    )

def get_species_distribution():

    df = load_animals()

    return (
        df["Species"]
        .value_counts()
        .to_dict()
    )
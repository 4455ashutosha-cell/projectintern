from database.data_loader import load_medicines

def get_all_medicines():

    df = load_medicines()

    return df.to_dict(
        orient="records"
    )

def search_medicine(name):

    df = load_medicines()

    result = df[
        df["Medicine_Name"]
        .str.contains(
            name,
            case=False,
            na=False
        )
    ]

    return result.to_dict(
        orient="records"
    )
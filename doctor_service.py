from database.data_loader import load_doctors

def get_all_doctors():

    df = load_doctors()

    return df.to_dict(
        orient="records"
    )

def get_doctors_by_state(state):

    df = load_doctors()

    result = df[
        df["State"].str.lower()
        ==
        state.lower()
    ]

    return result.to_dict(
        orient="records"
    )
import plotly.express as px

def specialization_chart(df):

    specialization = (
        df["Specialization"]
        .value_counts()
        .reset_index()
    )

    specialization.columns = [
        "Specialization",
        "Count"
    ]

    fig = px.sunburst(
        specialization,
        path=["Specialization"],
        values="Count",
        title="Doctor Specialization"
    )

    return fig


def state_doctors(df):

    state = (
        df["State"]
        .value_counts()
        .reset_index()
    )

    state.columns = [
        "State",
        "Count"
    ]

    fig = px.treemap(
        state,
        path=["State"],
        values="Count",
        title="Doctors by State"
    )

    return fig
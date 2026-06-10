import pandas as pd
import plotly.express as px

def disease_frequency(df):

    disease = (
        df["Disease"]
        .value_counts()
        .head(20)
        .reset_index()
    )

    disease.columns = [
        "Disease",
        "Cases"
    ]

    fig = px.bar(
        disease,
        x="Disease",
        y="Cases",
        title="Most Common Diseases"
    )

    return fig


def mortality_analysis(df):

    fig = px.scatter(
        df,
        x="Mortality",
        y="Recovery",
        color="Risk_Level",
        size="Mortality",
        title="Mortality vs Recovery"
    )

    return fig
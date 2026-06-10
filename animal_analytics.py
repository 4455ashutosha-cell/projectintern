import pandas as pd
import plotly.express as px

def species_distribution(df):

    species = (
        df["Species"]
        .value_counts()
        .reset_index()
    )

    species.columns = [
        "Species",
        "Count"
    ]

    fig = px.pie(
        species,
        names="Species",
        values="Count",
        title="Animal Species Distribution",
        hole=0.4
    )

    return fig


def breed_distribution(df):

    breed = (
        df["Breed"]
        .value_counts()
        .head(15)
        .reset_index()
    )

    breed.columns = [
        "Breed",
        "Count"
    ]

    fig = px.bar(
        breed,
        x="Breed",
        y="Count",
        title="Top Breeds"
    )

    return fig
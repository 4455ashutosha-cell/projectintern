import plotly.express as px

def milk_production(df):

    milk = (
        df.groupby("State")
        ["Milk_Yield_LPD"]
        .sum()
        .reset_index()
    )

    fig = px.bar(
        milk,
        x="State",
        y="Milk_Yield_LPD",
        title="Milk Production State Wise"
    )

    return fig


def milk_distribution(df):

    fig = px.box(
        df,
        x="Species",
        y="Milk_Yield_LPD",
        title="Milk Yield Distribution"
    )

    return fig
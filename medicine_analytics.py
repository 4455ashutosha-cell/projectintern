import plotly.express as px

def medicine_cost_analysis(df):

    fig = px.scatter(
        df,
        x="Cost_INR",
        y="Withdrawal_Period_Days",
        color="Risk_Level",
        hover_name="Medicine_Name",
        title="Medicine Cost vs Withdrawal Period"
    )

    return fig


def withdrawal_analysis(df):

    fig = px.histogram(
        df,
        x="Withdrawal_Period_Days",
        nbins=20,
        title="Withdrawal Period Analysis"
    )

    return fig
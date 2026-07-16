from dash import Dash, html, dcc, Input, Output
import pandas as pd
import plotly.express as px

# Read the data

df = pd.read_csv("formatted_sales_data.csv")

# Convert the date column to datetime
df["date"] = pd.to_datetime(df["date"])

# Sort the data by date

df = df.sort_values("date")



# Create the dash app

app = Dash(__name__)

# App layout

app.layout = html.Div([

    html.H1(
        "Soul Foods Sales Dashboard",
        style={
            "textAlign": "center",
            "color": "#E91E63"
        }
    ),

    dcc.RadioItems(
        id="region-filter",

        options=[
            {"label": "All", "value": "all"},
            {"label": "North", "value": "north"},
            {"label": "East", "value": "east"},
            {"label": "South", "value": "south"},
            {"label": "West", "value": "west"},
        ],

        value="all",

        inline=True,

        style={
            "textAlign": "center",
            "marginBottom": "20px"
        }
    ),

    dcc.Graph(id="sales-chart")

],
style={
    "padding": "30px",
    "fontFamily": "Arial",
    "backgroundColor": "#F5F5F5"
})



@app.callback(

    Output("sales-chart", "figure"),

    Input("region-filter", "value")

)

def update_graph(region):

    if region == "all":
        filtered_df = df
    else:
        filtered_df = df[df["region"] == region]

    fig = px.line(
        filtered_df,
        x="date",
        y="sales",
        title="Daily Sales"
    )

    fig.update_layout(
        xaxis_title="Date",
        yaxis_title="Sales"
    )

    return fig


# Run the app

if __name__ == "__main__":
    app.run(debug = True)

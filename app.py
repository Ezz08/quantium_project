from dash import Dash, html, dcc
import pandas as pd
import plotly.express as px

# Read the data

df = pd.read_csv("formatted_sales_data.csv")

# Convert the date column to datetime
df["date"] = pd.to_datetime(df["date"])

# Sort the data by date

df = df.sort_values("date")

# Create the Line chart

fig = px.line(
    df,
    x = "date",
    y = "sales",
    title = "Daily Sales"
)

# Update the graph

fig.update_layout(
    xaxis_title = "Date",
    yaxis_title = "Sales"
)

# Create the dash app

app = Dash(__name__)

# App layout

app.layout = html.Div([
    html.H1("Soul Foods Sales Dashboard"),

    dcc.Graph(
        figure = fig
    )
])

# Run the app

if __name__ == "__main__":
    app.run(debug = True)

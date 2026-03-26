# pages/home_cb.py
from dash import callback, Input, Output
import pandas as pd
import plotly.express as px

# Chargement des données pour le callback
df = pd.read_csv("datas/avocado.csv")
df["Date"] = pd.to_datetime(df["Date"])

@callback(
    Output('graphique-prix-historique', 'figure'),
    Input('region-filter', 'value'),
    Input('type-filter', 'value')
)
def update_graph(region_selected, type_selected):
    # Filtrage des données
    filtered_df = df[(df["region"] == region_selected) & (df["type"] == type_selected)]
    filtered_df = filtered_df.sort_values(by="Date")

    # Création du graphique mis à jour
    fig = px.line(
        filtered_df, 
        x="Date", 
        y="AveragePrice",
        title=f"Évolution des prix : {region_selected} ({type_selected})",
        labels={"AveragePrice": "Prix Moyen ($)", "Date": "Période"},
        template="plotly_white"
    )
    fig.update_traces(line_color='#2c3e50')
    return fig
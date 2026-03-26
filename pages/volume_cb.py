# pages/volume_cb.py
from dash import callback, Input, Output
import pandas as pd
import plotly.express as px

# Chargement des données
df = pd.read_csv("datas/avocado.csv")

@callback(
    Output('graphique-volume-bar', 'figure'),
    Input('volume-region-dropdown', 'value')
)
def update_volume_graph(regions_selected):
    # Si rien n'est sélectionné, on montre le top 10 par défaut
    if not regions_selected:
        df_plot = df[df["region"] != "TotalUS"].groupby("region")["Total Volume"].sum().sort_values(ascending=False).head(10).reset_index()
        title = "Top 10 des régions par Volume (Total)"
    else:
        # Sinon on filtre sur les régions choisies
        df_plot = df[df["region"].isin(regions_selected)].groupby("region")["Total Volume"].sum().reset_index()
        title = "Comparaison des Volumes par Région"

    fig = px.bar(
        df_plot, 
        x="region", 
        y="Total Volume",
        title=title,
        template="plotly_white",
        color_discrete_sequence=['#27ae60']
    )
    
    fig.update_layout(xaxis_title="Région", yaxis_title="Volume Total")
    return fig
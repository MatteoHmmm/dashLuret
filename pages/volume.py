# pages/volume.py
from dash import html, dcc
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px

# Chargement des données pour préparer le graphique par défaut
df = pd.read_csv("datas/avocado.csv")

# Liste des régions pour le futur filtre
liste_regions = sorted(df["region"].unique())

# Graphique de volume par défaut (Top 10 régions hors TotalUS)
df_volume = df[df["region"] != "TotalUS"].groupby("region")["Total Volume"].sum().sort_values(ascending=False).head(10).reset_index()
fig_vol = px.bar(df_volume, x="region", y="Total Volume", 
                 title="Top 10 des régions par Volume de ventes",
                 template="plotly_white", color_discrete_sequence=['#27ae60'])

layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.H1("Analyse des Volumes de Ventes", className="text-primary mt-4 mb-2"),
            html.Hr(),
            html.P("Cette page analyse les quantités d'avocats vendues par secteur.", className="lead"),
        ], width=12)
    ]),

    dbc.Row([
        # Sidebar de filtres (Visuel uniquement pour ce commit)
        dbc.Col([
            html.Div([
                html.H5("Filtres de Volume", className="border-bottom pb-2 mb-3"),
                
                html.Label("Comparer les régions :", className="small font-weight-bold"),
                dcc.Dropdown(
                    id='volume-region-dropdown',
                    options=[{'label': r, 'value': r} for r in liste_regions],
                    multi=True,
                    placeholder="Sélectionnez des régions...",
                    className="mb-3"
                ),

                html.Div([
                    html.Small("Les filtres seront activés au prochain commit.", 
                             className="text-warning font-italic")
                ], className="mt-4")
            ], className="p-4 shadow-sm border rounded bg-white")
        ], width=3),

        # Zone du graphique
        dbc.Col([
            html.Div([
                html.H5("Répartition Géographique", className="border-bottom pb-2 mb-3"),
                dcc.Graph(id='graphique-volume-bar', figure=fig_vol)
            ], className="p-4 shadow-sm border rounded bg-white")
        ], width=9)
    ])
], fluid=True, className="py-3")
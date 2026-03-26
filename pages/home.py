# pages/home.py
from dash import html, dcc, dash_table
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px

# --- PRÉPARATION DES DONNÉES ---
df = pd.read_csv("datas/avocado.csv")
df["Date"] = pd.to_datetime(df["Date"])
df = df.sort_values(by="Date")

# On extrait les listes uniques pour les filtres
liste_regions = sorted(df["region"].unique())
liste_types = df["type"].unique()

# Graphique par défaut (Global)
df_grouped = df.groupby("Date")["AveragePrice"].mean().reset_index()
fig_prix = px.line(df_grouped, x="Date", y="AveragePrice", template="plotly_white")
fig_prix.update_traces(line_color='#2c3e50')

layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.H1("Rapport d'Analyse : Marché des Avocats (USA)", className="text-primary mt-4 mb-2"),
            html.Hr(),
        ], width=12)
    ]),

    dbc.Row([
        # --- COLONNE DE GAUCHE : LES FILTRES ---
        dbc.Col([
            html.Div([
                html.H5("Paramètres de filtrage", className="border-bottom pb-2 mb-3"),
                
                # Filtre Région
                html.Label("Sélectionner une région :", className="small font-weight-bold"),
                dcc.Dropdown(
                    id='region-filter',
                    options=[{'label': r, 'value': r} for r in liste_regions],
                    value='TotalUS', # Valeur par défaut
                    clearable=False,
                    className="mb-3 text-dark"
                ),
                
                # Filtre Type
                html.Label("Type d'avocat :", className="small font-weight-bold"),
                dcc.Dropdown(
                    id='type-filter',
                    options=[{'label': t.capitalize(), 'value': t} for t in liste_types],
                    value='conventional',
                    clearable=False,
                    className="mb-3 text-dark"
                ),

                html.Div([
                    html.Small("Note : L'interaction sera activée au Commit 6.", 
                             className="text-info font-italic")
                ], className="mt-4")

            ], className="p-4 shadow-sm border rounded bg-white")
        ], width=3),

        # --- COLONNE DE DROITE : VISUALISATION ---
        dbc.Col([
            html.Div([
                html.H5("Analyse Temporelle des Prix", className="border-bottom pb-2 mb-3"),
                dcc.Graph(id='graphique-prix-historique', figure=fig_prix),
            ], className="p-4 shadow-sm border rounded bg-white")
        ], width=9)
    ])
], fluid=True, className="py-3")
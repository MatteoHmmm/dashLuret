import dash
dash.register_page(__name__, path='/infos') # L'adresse sera /infos

# pages/infos.py
from dash import html
import dash_bootstrap_components as dbc

layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.H1("Informations et Méthodologie", className="text-primary mt-4 mb-2"),
            html.Hr(),
        ], width=12)
    ]),

    dbc.Row([
        # Colonne de texte
        dbc.Col([
            html.Div([
                html.H4("À propos du projet", className="mb-3"),
                html.P([
                    "Ce dashboard a été conçu pour analyser les tendances du marché des avocats aux États-Unis entre 2015 et 2018. ",
                    "Il permet de visualiser l'évolution des prix moyens ainsi que les volumes de ventes par région."
                ]),
                html.H5("Source des données", className="mt-4"),
                html.P([
                    "Les données proviennent du ", 
                    html.A("Hass Avocado Board", href="https://hassavocadoboard.com/", target="_blank"),
                    " et ont été consolidées pour l'analyse."
                ]),
                html.Div([
                    html.Strong("Note technique : "),
                    html.Span("Application développée avec Python, Dash et Plotly.")
                ], className="alert alert-info mt-4")
            ])
        ], width=7),

        # Colonne Image (On utilise enfin ton fichier BG.jpg)
        dbc.Col([
            html.Div([
                html.Img(
                    src="/assets/BG.jpg", 
                    className="img-fluid rounded shadow",
                    style={"maxHeight": "400px", "width": "100%", "objectFit": "cover"}
                ),
                html.P("Crédit image : Dossier Assets", className="text-muted small text-center mt-2")
            ])
        ], width=5)
    ])
], fluid=True, className="py-3")
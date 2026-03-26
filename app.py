# app.py
from dash import Dash
import dash_bootstrap_components as dbc
from pages.home import layout

# Initialisation avec le thème LUX
app = Dash(__name__, external_stylesheets=[dbc.themes.LUX], use_pages=False)
app.title = "Analyse Marché Avocats"

app.layout = layout

if __name__ == "__main__":
    app.run(debug=True)
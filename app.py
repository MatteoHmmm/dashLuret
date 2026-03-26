# app.py
from dash import Dash
import dash_bootstrap_components as dbc
from pages.volume import layout # Pour l'instant on affiche toujours home par défaut

# IMPORTATION DES CALLBACKS (Pages 1 et 2)
import pages.home_cb 
import pages.volume_cb 

app = Dash(__name__, external_stylesheets=[dbc.themes.LUX], use_pages=False)
app.title = "Analyse Marché Avocats"
app.layout = layout

if __name__ == "__main__":
    app.run(debug=True)
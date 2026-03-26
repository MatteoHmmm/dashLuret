# app.py
from dash import Dash
import dash_bootstrap_components as dbc
from pages.infos import layout  # On importe la page infos pour ce commit

# Pas de callbacks pour cette page (elle est statique), mais on garde les imports
import pages.home_cb 
import pages.volume_cb 

app = Dash(__name__, external_stylesheets=[dbc.themes.LUX], use_pages=False)
app.title = "Analyse Marché Avocats"
app.layout = layout # On affiche la page Infos

if __name__ == "__main__":
    app.run(debug=True)
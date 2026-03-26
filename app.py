# app.py
from dash import Dash, html, page_container
import dash_bootstrap_components as dbc

# IMPORTATION DES CALLBACKS (Indispensable pour qu'ils soient actifs)
import pages.home_cb 
import pages.volume_cb 

# On active le mode multi-pages (use_pages=True)
app = Dash(__name__, external_stylesheets=[dbc.themes.LUX], use_pages=True)
app.title = "Avocado Analytics"

# Création de la barre de navigation
navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Analyse des Prix", href="/")),
        dbc.NavItem(dbc.NavLink("Analyse des Volumes", href="/volume")),
        dbc.NavItem(dbc.NavLink("Informations", href="/infos")),
    ],
    brand="AVOCADO MARKET REPORT",
    brand_href="/",
    color="primary",
    dark=True,
    className="mb-4"
)

# Le layout de base contient la Navbar + le contenu de la page actuelle
app.layout = html.Div([
    navbar,
    page_container # C'est ici que Dash injecte le contenu de home, volume ou infos
])

if __name__ == "__main__":
    app.run(debug=True)
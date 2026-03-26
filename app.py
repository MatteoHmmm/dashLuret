# app.py
from dash import Dash, html, page_container
import dash_bootstrap_components as dbc
import pages.home_cb 
import pages.volume_cb 

app = Dash(__name__, external_stylesheets=[dbc.themes.LUX], use_pages=True)
app.title = "Avocado Analytics Pro"

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

# Ajout d'un Footer
footer = html.Footer(
    dbc.Container(
        html.P("© 2024 - Projet Dash Avocado - Réalisé dans le cadre du module MECEN", 
               className="text-center text-muted border-top pt-3 mt-5"),
    )
)

app.layout = html.Div([
    navbar,
    page_container,
    footer
])

if __name__ == "__main__":
    app.run(debug=True)
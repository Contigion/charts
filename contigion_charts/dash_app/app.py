from dash import Dash, page_container
from dash.html import Div
import dash_bootstrap_components as dbc
from contigion_charts.components.container import background


def initialise_app():
    app = Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.icons.BOOTSTRAP])
    app.layout = Div([
        background(),
        page_container
    ])

    return app

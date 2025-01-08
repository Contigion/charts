from dash import Dash, page_container
from dash.html import Div
from dash_bootstrap_components.themes import BOOTSTRAP as BOOTSRAP_THEME
from dash_bootstrap_components.icons import BOOTSTRAP as BOOTSRAP_ICONS
from contigion_charts.components.container import background


def initialise_app():
    app = Dash(__name__, use_pages=True, external_stylesheets=[BOOTSRAP_THEME, BOOTSRAP_ICONS])
    app.layout = Div([
        background(),
        page_container
    ])

    return app

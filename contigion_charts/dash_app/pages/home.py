import dash
from dash.dependencies import Input, Output, State

from contigion_metatrader import get_timeframe_value, get_market_data, get_symbol_names, get_timeframes
from contigion_charts.components import (page, container_row, content_container_col, dropdown, number_input, get_chart,
                                         button, title, checklist, icon_button, text, content_container_row)

dash.register_page(__name__,
                   path='/',
                   title='Contigion Charts',
                   name='charts'
                   )


def layout():
    symbol = 'USDJPYmicro'
    timeframe = get_timeframe_value('M15')
    n_candles = 500
    step = 10
    data = get_market_data(symbol, timeframe, n_candles)

    symbols = get_symbol_names()
    timeframes = get_timeframes()
    indicators = [{'label': 'A', 'value': 'A'},{'label': 'B', 'value': 'B'},{'label': 'C', 'value': 'C'},]

    chart_title = container_row([
        title('chart-title', f'{symbol} {timeframe} Chart', 'bold-text')
    ])

    side_panel = content_container_col(children=[
        dropdown('symbol-dropdown', 'Symbol', symbol, symbols, 'bold-text'),
        dropdown('timeframe-dropdown', 'Timeframes', timeframe, timeframes, 'bold-text'),
        number_input('n-candles-input', 'Number of Candles', n_candles, step, minimum=n_candles, class_name='bold-text'),
        button('update-chart', 'Update Chart')
    ])

    side_panel_2 = content_container_col(children=[
        checklist('indicator-checklist', 'Indicators', [], indicators, 'bold-text')
    ])

    side_panel_3 = content_container_row(children=[
        icon_button('controls-previous', 'bi bi-rewind-fill'),
        icon_button('controls-play', 'bi bi-play-fill'),
        icon_button('controls-stop', 'bi bi-stop-fill'),
        icon_button('controls-next', 'bi bi-fast-forward-fill'),
        icon_button('controls-decrease', 'bi bi-dash'),
        text('controls-increase', 'Speed x1'),
        icon_button('controls-increase', 'bi bi-plus'),
    ], class_name='container-centered')

    home_content = container_row(children=[
        get_chart(symbol, data),
        side_panel,
        side_panel_2,
        side_panel_3
    ], class_name='full-width full-height')

    home_page = page(page_id='home-page', children=[
        chart_title,
        home_content
    ])

    return home_page


# def layout():
#     page = html.Div([
#         comp.background(),
#         html.P("Sandbox", className="page-title"),
#         comp.chart_options_row(),
#
#         html.Div([
#             html.P("", id="sandbox-chart-title", className="page-title"),
#             html.Button('Refresh Chart', id='refresh-chart-button', className='control-button purple', n_clicks=0)
#         ], className="row-container"),
#
#         html.Div([], className="chart-container", id="sandbox-graph-container"),
#
#     ], className="page")
#
#     return page


# @dash.callback(
#     [Output('sandbox-chart-title', 'children'),
#      Output('sandbox-graph-container', 'children')],
#     Input('refresh-chart-button', 'n_clicks'),
#     State('symbol-dropdown', 'value'),
#     State('timeframe-dropdown', 'value'),
#     State('strategy-dropdown', 'value'),
#     State('number-candles-input', 'value')
# )
# def graph(n_clicks, symbol, timeframe, strategy, number_of_candles):
#     chart_title = f"{symbol} {timeframe} Chart"
#
#     adjust = 6
#     candles = int(number_of_candles) + adjust
#     timeframe = get_timeframe_value()[timeframe]
#
#     return chart_title, comp.sandbox_chart(symbol, timeframe, strategy, candles)

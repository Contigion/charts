import dash
from dash.dependencies import Input, Output, State

from contigion_metatrader import get_timeframe_value, get_market_data, get_symbol_names, get_timeframes
from contigion_charts.components import (page, container_row, content_container_col, dropdown, number_input, get_chart,
                                         button, title)

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

    chart_title = container_row([
        title('chart-title', f'{symbol} {timeframe} Chart', 'bold-text')
    ])

    side_panel = content_container_col(children=[
        dropdown('symbol-dropdown', 'Symbol', symbol, symbols, 'bold-text'),
        dropdown('timeframe-dropdown', 'Timeframes', timeframe, timeframes, 'bold-text'),
        number_input('n-candles-input', 'Number of Candles', n_candles, step, minimum=n_candles, className='bold-text'),
        button('update-chart', 'Update Chart')
    ])

    home_content = container_row(children=[
        get_chart(symbol, data),
        side_panel
    ], className='full-width full-height')

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


@dash.callback(
    [Output('sandbox-chart-title', 'children'),
     Output('sandbox-graph-container', 'children')],
    Input('refresh-chart-button', 'n_clicks'),
    State('symbol-dropdown', 'value'),
    State('timeframe-dropdown', 'value'),
    State('strategy-dropdown', 'value'),
    State('number-candles-input', 'value')
)
def graph(n_clicks, symbol, timeframe, strategy, number_of_candles):
    chart_title = f"{symbol} {timeframe} Chart"

    adjust = 6
    candles = int(number_of_candles) + adjust
    timeframe = get_timeframe_value()[timeframe]

    return chart_title, comp.sandbox_chart(symbol, timeframe, strategy, candles)

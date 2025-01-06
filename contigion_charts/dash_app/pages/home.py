from datetime import datetime

from dash import register_page, callback, Output, Input, State
from contigion_metatrader import get_timeframe_value, get_market_data, get_symbol_names, get_timeframes
from dash.html import Div

from contigion_charts.components import (page, container_row, content_container_col, dropdown, number_input, get_chart,
                                         button, title, checklist, icon_button, text, content_container_row, container,
                                         container_col)

register_page(__name__, path='/', title='Contigion Charts', name='charts')


def layout():
    symbol = 'USDJPYmicro'
    timeframe = 'M15'
    n_candles = 500
    step = 10
    data = get_market_data(symbol, get_timeframe_value(timeframe), n_candles)

    symbols = get_symbol_names()
    timeframes = get_timeframes()
    indicators = [{'label': 'A', 'value': 'A'}, {'label': 'B', 'value': 'B'}, {'label': 'C', 'value': 'C'}, ]

    chart_container = container([
        get_chart(symbol, data),
    ])
    chart_container.id = 'chart-container'

    chart_params = content_container_col(children=[
        dropdown('symbol-dropdown', 'Symbol', symbol, symbols, 'bold-text'),
        dropdown('timeframe-dropdown', 'Timeframes', timeframe, timeframes, 'bold-text'),
        number_input('n-candles-input', 'Number of Candles', n_candles, step, minimum=10,
                     class_name='bold-text'),
        button('update-chart', 'Update Chart')
    ])

    indicator_panel = content_container_col(children=[
        checklist('indicator-checklist', 'Indicators', [], indicators, 'bold-text')
    ])

    control_panel = content_container_row(children=[
        icon_button('controls-previous', 'bi bi-rewind-fill'),
        icon_button('controls-play-stop', 'bi bi-play-fill green-icon-button'),
        icon_button('controls-next', 'bi bi-fast-forward-fill'),
        icon_button('controls-decrease', 'bi bi-dash'),
        text('controls-current-index', 'Candle 0'),
        icon_button('controls-increase', 'bi bi-plus'),
    ], class_name='container-centered')

    home_content = container_row(children=[
        chart_container,
        chart_params,
        indicator_panel,
        control_panel
    ], class_name='full-width full-height')

    chart_title = container([
        title('chart-title', f'{symbol} {timeframe} Chart', 'bold-text'),
        text('chart-last-update', f'{get_current_time()}', 'white')
    ])

    home_page = page(page_id='home-page', children=[
        chart_title,
        home_content
    ])

    return home_page


@callback(
    [
        Output('chart-title', 'children'),
        Output('chart-last-update', 'children'),
        Output('chart-container', 'children')

    ],
    Input('update-chart', 'n_clicks'),
    State('symbol-dropdown', 'value'),
    State('timeframe-dropdown', 'value'),
    State('n-candles-input', 'value'),
    prevent_initial_call=True
)
def update_chart(_, symbol, timeframe, n_candles):
    if symbol is None or timeframe is None or n_candles is None:
        raise ValueError(f"{__file__}: {update_chart.__name__}\n"
                         f"Unable to update chart: symbol={symbol}, timeframe={timeframe}, n_candles={n_candles}\n")

    chart_title = f"{symbol} {timeframe} Chart"
    last_update = get_current_time()

    data = get_market_data(symbol, get_timeframe_value(timeframe), n_candles)
    chart = get_chart(symbol, data)

    return [chart_title], [last_update], [chart]


@callback(
    Input('controls-previous', 'n_clicks'),
    prevent_initial_call=True
)
def controls_previos(n_clicks):
    print('previous <<')


@callback(
    Input('controls-next', 'n_clicks'),
    prevent_initial_call=True
)
def controls_next(n_clicks):
    print('next >>')


@callback(
    Output('controls-play-stop', 'className'),
    Input('controls-play-stop', 'n_clicks'),
    State('controls-play-stop', 'className'),
    prevent_initial_call=True
)
def controls_play_stop(_, current_classes):
    classes = current_classes

    if 'play' in current_classes:
        classes = current_classes.replace('play', 'stop').replace('green', 'red')
        return classes

    elif 'stop' in current_classes:
        classes = current_classes.replace('stop', 'play').replace('red', 'green')
        return classes

    return classes


@callback(
    Output('controls-current-index', 'children'),
    Input('controls-decrease', 'n_clicks'),
    State('controls-current-index', 'children'),
    prevent_initial_call=True
)
def controls_decrease(_, component_text):
    c = component_text.split(' ')
    prefix = c[0]
    index = int(c[1])

    if index > 0:
        return f'{prefix} {index - 1}'

    return component_text


@callback(
    Output('controls-current-index', 'children'),
    Input('controls-increase', 'n_clicks'),
    State('controls-current-index', 'children'),
    State('n-candles-input', 'value'),
    prevent_initial_call=True
)
def controls_increase(_, component_text, n_candles):
    if n_candles is None:
        raise ValueError(f"{__file__}: {update_chart.__name__}\n"
                         f"Unable to update index: n_candles={n_candles}\n")

    c = component_text.split(' ')
    prefix = c[0]
    index = int(c[1])

    if (index + 1) < n_candles:
        return f'{prefix} {index + 1}'

    return component_text


def get_current_time():
    current_date = datetime.now()
    current_time = current_date.strftime('%H:%M:%S')
    current_day = current_date.strftime('%a')
    current_date_str = current_date.strftime('%d %b')

    return f"{current_day}, {current_date_str} - {current_time}"

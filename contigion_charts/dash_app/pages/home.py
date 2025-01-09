from dash import register_page, callback, Output, Input, State, callback_context, no_update
from dash.dcc import Interval
from contigion_metatrader import get_timeframe_value, get_market_data, get_symbol_names, get_timeframes
from contigion_charts.components import (page, container_row, content_container_col, dropdown, number_input, live_chart,
                                         button, title, checklist, text, content_container_row, container,
                                         container_col, link)
from contigion_charts.components.button import switch
from contigion_charts.config import CHART_REFRESH_INTERVAL_MS, MIN_CANDLES
from contigion_charts.util import get_current_time
from contigion_charts.util.indicators import get_indicators

register_page(__name__, path='/', title='Contigion Charts', name='charts')

# Defaults
SYMBOL = 'USDJPYmicro'
TIMEFRAME = 'M15'
N_CANDLES = 500
STEP = 10


def layout():
    data = get_market_data(SYMBOL, get_timeframe_value(TIMEFRAME), N_CANDLES, False)
    symbols = get_symbol_names()
    timeframes = get_timeframes()
    indicators = get_indicators()

    chart_title = container_col([
        title('chart-title', f'{SYMBOL} {TIMEFRAME} Chart', 'bold-text'),
        text('chart-last-update', f'{get_current_time()}')
    ])

    chart_params = content_container_col(children=[
        dropdown('symbol-dropdown', 'Symbol', SYMBOL, symbols, 'bold-text'),
        dropdown('timeframe-dropdown', 'Timeframes', TIMEFRAME, timeframes, 'bold-text'),
        number_input('n-candles-input', 'Number of Candles', N_CANDLES, STEP, MIN_CANDLES,
                     class_name='bold-text'),
        switch('live-switch', 'Live Chart'),
        button('update-chart', 'Update Chart')
    ])

    indicator_panel = content_container_col(children=[
        checklist('indicator-checklist', 'Indicators', [], indicators, 'bold-text')
    ])

    control_panel = content_container_row(children=[
        link('visualise-your-data-button', 'Visualise your strategy', '/visualise', 'button')
    ], class_name='container-centered')

    chart_container = container([
        live_chart(SYMBOL, data, []),
    ], class_name='left')
    chart_container.id = 'chart-container'

    right_container = container_col(children=[
        control_panel,
        indicator_panel,
        chart_params
    ], class_name='right')

    home_content = container_row(children=[
        chart_container,
        right_container
    ], class_name='page-container')

    home_page = page(page_id='home-page', children=[
        chart_title,
        home_content,
        Interval('chart-refresh', interval=CHART_REFRESH_INTERVAL_MS)
    ])

    return home_page


@callback(
    Output('chart-title', 'children'),
    Output('chart-last-update', 'children'),
    Output('chart-container', 'children'),
    [Input('update-chart', 'n_clicks'),
     Input('chart-refresh', 'n_intervals')],
    State('symbol-dropdown', 'value'),
    State('timeframe-dropdown', 'value'),
    State('n-candles-input', 'value'),
    State('indicator-checklist', 'value'),
    State('live-switch', 'on'),
    prevent_initial_call=True
)
def update_chart(_, __, symbol, timeframe, n_candles, selected_indicators, is_live_update):
    if (symbol is None) or (timeframe is None) or (n_candles is None):
        raise ValueError(f"{__file__}: {update_chart.__name__}\n"
                         f"Unable to update chart: symbol={symbol}, timeframe={timeframe}, n_candles={n_candles}\n")

    triggered_context = callback_context.triggered[0]['prop_id'].split('.')[0]

    if not is_live_update and triggered_context == 'chart-refresh':
        return no_update, no_update, no_update

    indicators = [indicator for indicator in selected_indicators if indicator]

    chart_title = f"{symbol} {timeframe} Chart"
    last_update = get_current_time()

    data = get_market_data(symbol, get_timeframe_value(timeframe), n_candles, False)
    chart = live_chart(symbol, data, indicators)

    return chart_title, last_update, chart

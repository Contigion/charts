from plotly.graph_objects import Scatter
from MetaTrader5 import symbol_info_tick
from contigion_charts.config import RED, YELLOW_LIME, MAIN_PURPLE, LIME_GREEN, MAIN_PINK, MAIN_BLUE, SKY_BLUE, ORANGE

BULL = SKY_BLUE
BEAR = ORANGE


def add_plot(mode, data, label, chart, color, plot_name, point_label):
    chart.add_trace(
        Scatter(
            x=data['time'],
            y=data[label],
            mode=mode,
            marker={'color': color},
            name=plot_name,
            text=point_label
        )
    )


def add_line_plot(data, label, chart, color, plot_name):
    add_plot('lines', data, label, chart, color, plot_name, '')


def add_scatter_plot(data, label, chart, color, plot_name, point_label=''):
    add_plot('markers', data, label, chart, color, plot_name, point_label)


def plot_sma_crossover(function, data, fast, slow, chart):
    sma_data = function(data, fast, slow)
    add_line_plot(sma_data, 'sma_slow', chart, RED, f'Slow Sma {slow}')
    add_line_plot(sma_data, 'sma_fast', chart, YELLOW_LIME, f'Fast Sma {fast}')


def plot_bollinger_bands(function, data, period, chart):
    bb_data = function(data, period)
    add_line_plot(bb_data, 'lower', chart, MAIN_PINK, 'BB Lower')
    add_line_plot(bb_data, 'upper', chart, MAIN_PINK, 'BB Upper')
    add_line_plot(bb_data, 'mavg', chart, MAIN_PINK, 'BB Middle')


def plot_supertrend(data, chart, plot_name):
    add_line_plot(data, 'supertrend', chart, MAIN_BLUE, plot_name)


def plot_psar(data, chart, plot_name):
    add_scatter_plot(data, 'psar_up', chart, MAIN_PURPLE, plot_name)
    add_scatter_plot(data, 'psar_down', chart, MAIN_PURPLE, plot_name)


def plot_snr(data, chart):
    _, support, resistance = data
    add_scatter_plot(support, 'level', chart, LIME_GREEN, 'Support')
    add_scatter_plot(resistance, 'level', chart, RED, 'Resistance')


def plot_signals(data, chart, plot_name, point_label=None):
    buy_signals = data[data['signal'] == 'buy']
    sell_signals = data[data['signal'] == 'sell']
    buy_label = buy_signals[point_label] if point_label else ''
    sell_label = sell_signals[point_label] if point_label else ''

    add_scatter_plot(buy_signals, 'close', chart, BULL, f'Buy {plot_name}', buy_label)
    add_scatter_plot(sell_signals, 'close', chart, BEAR, f'Sell {plot_name}', sell_label)


def plot_current_price(symbol, chart):
    tick = symbol_info_tick(symbol)

    chart.add_hline(y=tick.ask, line_width=1, line_color=BULL)
    chart.add_hline(y=tick.bid, line_width=1, line_color=BEAR)

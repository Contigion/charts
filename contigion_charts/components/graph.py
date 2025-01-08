from pandas import date_range
from MetaTrader5 import symbol_info_tick
import plotly.graph_objects as go
from dash.dcc import Graph
from contigion_charts.config import (BACKGROUND, BULLISH_CANDLE_FILL, BULLISH_CANDLE_OUTLINE, BEARISH_CANDLE_FILL,
                                     BEARISH_CANDLE_OUTLINE, RED, YELLOW_LIME, SKY_BLUE, ORANGE, MAIN_PURPLE,
                                     LIME_GREEN, MAIN_PINK, MAIN_BLUE, SMA_FAST, SMA_SLOW, BOLLINGER_BANDS_PERIOD)
from contigion_charts.util.indicators import get_indicator_function

BULL = SKY_BLUE
BEAR = ORANGE


def get_chart(symbol, data, indicators):
    chart = go.Figure(
        data=[
            go.Candlestick(
                x=data['time'],
                open=data['open'],
                high=data['high'],
                low=data['low'],
                close=data['close']
            )
        ]
    )

    for indicator in indicators:
        function = get_indicator_function(indicator)

        if indicator == 'SMA Crossover':
            plot_sma_crossover(function, data, SMA_FAST, SMA_SLOW, chart)

        elif indicator == 'Bollinger Bands':
            plot_bollinger_bands(function, data, BOLLINGER_BANDS_PERIOD, chart)

        result = function(data)
        point_label = ''

        if indicator == 'Supertrend':
            plot_supertrend(result, chart, indicator)
            continue

        elif indicator == 'PSAR':
            plot_psar(result, chart, indicator)
            continue

        elif indicator == 'Support and Resistence':
            plot_snr(result, chart)
            continue

        elif indicator in ['Candle Type', 'Candle Patterns (1x)', 'Candle Patterns (2x)', 'Candle Patterns (3x)']:
            point_label = 'pattern'

        plot_signals(result, chart, indicator, point_label)

    plot_current_price(symbol, chart)
    configure_chart(chart)
    remove_breaks(data, chart)

    graph = Graph(
        figure=chart,
        config={'displayModeBar': True, 'scrollZoom': True},
        className='graph'
    )

    return graph


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


def add_line_plot(data, label, chart, color, plot_name):
    chart.add_trace(
        go.Scatter(
            x=data['time'],
            y=data[label],
            mode='lines',
            marker=dict(color=color),
            name=plot_name
        )
    )


def add_scatter_plot(data, label, chart, color, plot_name, point_label=''):
    chart.add_trace(
        go.Scatter(
            x=data['time'],
            y=data[label],
            mode='markers',
            marker=dict(color=color),
            name=plot_name,
            text=point_label
        )
    )


def configure_chart(chart):
    # Background colour
    chart.update_layout(paper_bgcolor=BACKGROUND)
    chart.update_layout(plot_bgcolor=BACKGROUND)

    # Disable grid
    chart.update_xaxes(showgrid=False)
    chart.update_yaxes(showgrid=False)

    # Candle colour
    cs = chart.data[0]
    cs.increasing.fillcolor = BULLISH_CANDLE_FILL
    cs.increasing.line.color = BULLISH_CANDLE_OUTLINE
    cs.decreasing.fillcolor = BEARISH_CANDLE_FILL
    cs.decreasing.line.color = BEARISH_CANDLE_OUTLINE

    chart.update_layout(xaxis_rangeslider_visible=False, yaxis={'side': 'left'}, dragmode='pan')
    chart.layout.xaxis.fixedrange = False
    chart.layout.yaxis.fixedrange = False


def remove_breaks(data, chart):
    time_diffs = data['time'].diff().dropna()
    interval = time_diffs.min()

    full_range = date_range(start=data['time'].min(), end=data['time'].max(), freq=interval)
    missing_timestamps = full_range.difference(data['time'])

    chart.update_xaxes(
        rangebreaks=[
            dict(values=missing_timestamps.strftime('%Y-%m-%d %H:%M:%S').tolist())
        ]
    )

from pandas import date_range
import plotly.graph_objects as go
from dash.dcc import Graph
from contigion_charts.config import (BACKGROUND, BULLISH_CANDLE_FILL, BULLISH_CANDLE_OUTLINE, BEARISH_CANDLE_FILL,
                                     BEARISH_CANDLE_OUTLINE, SMA_FAST, SMA_SLOW, BOLLINGER_BANDS_PERIOD)
from contigion_charts.util.graph import (plot_sma_crossover, plot_bollinger_bands, plot_supertrend, plot_psar, plot_snr,
                                         plot_signals, plot_current_price)
from contigion_charts.util.indicators import get_indicator_function


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

        if indicator == 'PSAR':
            plot_psar(result, chart, indicator)
            continue

        if indicator == 'Support and Resistence':
            plot_snr(result, chart)
            continue

        if indicator in ['Candle Type', 'Candle Patterns (1x)', 'Candle Patterns (2x)', 'Candle Patterns (3x)']:
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
            {'values': missing_timestamps.strftime('%Y-%m-%d %H:%M:%S').tolist()}
        ]
    )

from MetaTrader5 import symbol_info_tick
import plotly.graph_objects as go
from dash.dcc import Graph

from contigion_charts.components.config import (BACKGROUND, BULLISH_CANDLE_FILL, BULLISH_CANDLE_OUTLINE,
                                                BEARISH_CANDLE_FILL, BEARISH_CANDLE_OUTLINE, BLACK, RED, YELLOW_LIME,
                                                SKY_BLUE, ORANGE)
from contigion_charts.dash_app.util.indicators import get_indicator_function


def get_chart(symbol, data, indicators):
    # Tick data
    tick = symbol_info_tick(symbol)

    # Chart
    chart = go.Figure(
        data=[
            go.Candlestick(x=data.index, open=data['open'], high=data['high'], low=data['low'], close=data['close'])])

    # Combine plots
    for indicator in indicators:
        func = get_indicator_function(indicator)
        result = func(data)

        if indicator == 'SMA Crossover':
            chart.add_trace(go.Scatter(x=result.index, y=result['sma_slow'], mode='lines',
                                       marker=dict(color=RED), name='Slow SMA'))
            chart.add_trace(go.Scatter(x=result.index, y=result['sma_fast'], mode='lines',
                                       marker=dict(color=YELLOW_LIME), name='Fast Sma'))

        buy_signals = result[result['signal'] == 'buy']
        sell_signals = result[result['signal'] == 'sell']

        chart.add_trace(go.Scatter(x=buy_signals.index, y=buy_signals['close'], mode='markers',
                                   marker=dict(color=SKY_BLUE), name='Buy'))
        chart.add_trace(go.Scatter(x=sell_signals.index, y=sell_signals['close'], mode='markers',
                                   marker=dict(color=ORANGE), name='Sell'))

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

    # Add current price
    chart.add_hline(y=tick.ask, line_width=1, line_color=BLACK)
    chart.add_hline(y=tick.bid, line_width=1, line_color=BLACK)

    chart.update_layout(xaxis_rangeslider_visible=False, yaxis={'side': 'right'}, dragmode='pan')
    chart.layout.xaxis.fixedrange = False
    chart.layout.yaxis.fixedrange = False

    return Graph(figure=chart, config={'displayModeBar': True, 'scrollZoom': True}, className='graph')

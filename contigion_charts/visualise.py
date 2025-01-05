import plotly.graph_objects as go

from contigion_charts.config import BACKGROUND, BULLISH_CANDLE_FILL, BULLISH_CANDLE_OUTLINE, BEARISH_CANDLE_FILL, \
    BEARISH_CANDLE_OUTLINE, INDICATOR_LINE


def style_chart(chart):
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

    chart.update_layout(xaxis_rangeslider_visible=False, dragmode='pan')
    chart.layout.xaxis.fixedrange = False
    chart.layout.yaxis.fixedrange = False

    return chart


def visualise_chart(data):
    candlesticks = go.Candlestick(
        x=data['time'],
        open=data['open'],
        high=data['high'],
        low=data['low'],
        close=data['close'],
        name='Candlesticks'
    )

    # indicator = go.Scatter(
    #     x=data['time'],
    #     y=data['indicator'],
    #     mode='lines',
    #     name='indicator',
    #     line=dict(color=INDICATOR_LINE, width=2)
    # )

    layout = go.Layout(
        title='Candlestick Chart',
        xaxis=dict(title='Index'),
        yaxis=dict(title='Price'),
    )

    chart = go.Figure(data=[candlesticks], layout=layout)
    chart = style_chart(chart)

    chart.show()

    return


def multi_scatter_visualise(data, scatter_data, title):
    candlesticks = go.Candlestick(
        x=data['time'],
        open=data['open'],
        high=data['high'],
        low=data['low'],
        close=data['close'],
        name='Candlesticks'
    )

    layout = go.Layout(
        title=title,
        xaxis=dict(title='Time'),
        yaxis=dict(title='Price'),
    )

    combined_plot_data = go.Figure(candlesticks).data

    for sd in scatter_data:
        combined_plot_data += sd.data

    chart = go.Figure(data=combined_plot_data, layout=layout)
    chart = style_chart(chart)

    return chart
from contigion_indicators import sma, macd_crossover, psar
from contigion_metatrader import get_market_data, get_timeframe_value


def strategy(symbol='USDJPYmicro', timeframe='M15', number_of_candles=500):
    data = get_market_data(symbol, get_timeframe_value(timeframe), number_of_candles, False)
    data['line_y'] = sma(data, 21)['sma']
    data['point_y'] = psar(data)['psar_up']
    data['signal'] = macd_crossover(data)['signal']

    return data

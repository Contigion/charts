from contigion_indicators import (macd_crossover, psar_trend, rsi_signal, rsi_mavg, rsi_over_bought_sold, supertrend,
                                  bollinger_bands_cross, supertrend_trend, sma_crossover, sma_trend,
                                  triple_candlestick_pattern, support_and_resistance,
                                  candlestick_type, single_candlestick_pattern, dual_candlestick_pattern)

indicator_map = {
    'Bollinger Bands': bollinger_bands_cross,
    'SMA Crossover': sma_crossover,
    'SMA Direction': sma_trend,
    'Supertrend': supertrend,

    'RSI': rsi_signal,
    'RSI Moving Average': rsi_mavg,
    'RSI Overbought Oversold': rsi_over_bought_sold,
    'MACD Crossover': macd_crossover,

    'Supertrend Direction': supertrend_trend,
    'PSAR': psar_trend,
    'Candle Type': candlestick_type,
    'Candle Patterns (1x)': single_candlestick_pattern,
    'Candle Patterns (2x)': dual_candlestick_pattern,
    'Candle Patterns (3x)': triple_candlestick_pattern,
    'Support and Resistence': support_and_resistance,
}


def get_indicators():
    return list(indicator_map.keys())


def get_indicator_function(indicator):
    return indicator_map[indicator]

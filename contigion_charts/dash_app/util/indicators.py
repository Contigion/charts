from contigion_indicators import (macd_crossover, psar_trend, rsi, rsi_mavg, rsi_over_bought_sold, supertrend,
                                  bollinger_bands, supertrend_direction, sma_crossover, sma_trend_direction,
                                  triple_candlestick_pattern, get_support_and_resistance_levels,
                                  candlestick_type, single_candlestick_pattern, dual_candlestick_pattern)
from contigion_indicators import trading_session, day_of_the_week

indicator_map = {
    'Bollinger Bands': bollinger_bands,
    'SMA Crossover': sma_crossover,
    'SMA Direction': sma_trend_direction,
    'Supertrend': supertrend,

    'RSI': rsi,
    'RSI Moving Average': rsi_mavg,
    'RSI Overbought Oversold': rsi_over_bought_sold,
    'MACD Crossover': macd_crossover,

    'Supertrend Direction': supertrend_direction,
    'PSAR': psar_trend,
    'Candle Type': candlestick_type,
    'Candle Patterns (1x)': single_candlestick_pattern,
    'Candle Patterns (2x)': dual_candlestick_pattern,
    'Candle Patterns (3x)': triple_candlestick_pattern,
    'Support and Resistence': get_support_and_resistance_levels,
}


def get_indicators():
    return list(indicator_map.keys())


def get_indicator_function(indicator):
    return indicator_map[indicator]

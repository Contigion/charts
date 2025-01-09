from contigion_indicators import sma, macd_crossover, psar
from contigion_metatrader import get_market_data, get_timeframe_value, connect, disconnect
from contigion_utils import save_dataframe, print_error


def strategy(symbol='USDJPYmicro', timeframe='M15', number_of_candles=500):
    data = get_market_data(symbol, get_timeframe_value(timeframe), number_of_candles, False)
    data['line_y'] = sma(data, 21)['sma']
    data['point_y'] = psar(data)['psar_up']
    data['signal'] = macd_crossover(data)['signal']

    return data


if __name__ == '__main__':
    try:
        filename = 'strategy_data'

        connect()
        strategy_data = strategy()
        save_dataframe(filename, strategy_data)

    except RuntimeError as e:
        print_error(f"{__file__}: {__name__}")
        print_error(f"Runtime error: {e} \n")

    except Exception as e:
        print_error(f"{__file__}: {__name__}")
        print_error(f"An unexpected error occurred: {e} \n")

    finally:
        disconnect()

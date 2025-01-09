from contigion_metatrader import connect, disconnect
from contigion_utils import print_error, save_dataframe
from contigion_charts.dash_app.app import initialise_app
from contigion_charts.strategy import strategy


def generate_strategy_data():
    filename = 'strategy_data'
    strategy_data = strategy()
    save_dataframe(filename, strategy_data)


def run_dash_app():
    app = initialise_app()
    app.run_server()


if __name__ == '__main__':
    try:
        connect()
        generate_strategy_data()
        run_dash_app()

    except RuntimeError as e:
        print_error(f"{__file__}: {__name__}")
        print_error(f"Runtime error: {e} \n")

    except Exception as e:
        print_error(f"{__file__}: {__name__}")
        print_error(f"An unexpected error occurred: {e} \n")

    finally:
        disconnect()

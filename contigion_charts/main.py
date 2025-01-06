from contigion_metatrader import get_market_data, connect, disconnect
from contigion_utils import print_error

from contigion_charts.dash_app.app import initialise_app



from dash import Dash, html, page_container, Input, Output, callback





@callback(
    Output('navbar-time', 'children'),
    Input('time-update', 'n_intervals')
)
def update_time(n_intervals):
    return "hello"


if __name__ == '__main__':
    try:
        connect()

        app = initialise_app()
        app.run_server()

    except RuntimeError as e:
        print_error(f"{__file__}: {__name__}")
        print_error(f"Runtime error: {e} \n")

    except Exception as e:
        print_error(f"{__file__}: {__name__}")
        print_error(f"An unexpected error occurred: {e} \n")

    finally:
        disconnect()

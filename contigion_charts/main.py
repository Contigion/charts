from contigion_metatrader import connect, disconnect
from contigion_utils import print_error
from contigion_charts.dash_app.app import initialise_app

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

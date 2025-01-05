from contigion_metatrader import get_market_data, connect, disconnect
from contigion_utils import print_error
from visualise import visualise_chart

if __name__ == '__main__':
    try:
        connect()
        data = get_market_data()
        visualise_chart(data)

    except RuntimeError as e:
        print_error(f"{__file__}: {__name__}")
        print_error(f"Runtime error: {e} \n")

    except Exception as e:
        print_error(f"{__file__}: {__name__}")
        print_error(f"An unexpected error occurred: {e} \n")

    finally:
        disconnect()

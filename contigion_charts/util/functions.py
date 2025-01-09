import base64
from datetime import datetime
from io import StringIO
from pandas import read_csv


def get_current_time():
    current_date = datetime.now()
    current_time = current_date.strftime('%H:%M:%S')
    current_day = current_date.strftime('%a')
    current_date_str = current_date.strftime('%d %b')

    return f'{current_day}, {current_date_str} - {current_time}'


def parse_csv_data(content):
    _, content_string = content.split(',')
    decoded = base64.b64decode(content_string)
    try:
        return read_csv(StringIO(decoded.decode('utf-8')))

    except Exception as e:
        raise Exception(f'{__file__}: {parse_csv_data.__name__}\n'
                        f'There was an error processing this file: {e}')

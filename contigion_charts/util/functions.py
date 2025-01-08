from datetime import datetime


def get_current_time():
    current_date = datetime.now()
    current_time = current_date.strftime('%H:%M:%S')
    current_day = current_date.strftime('%a')
    current_date_str = current_date.strftime('%d %b')

    return f"{current_day}, {current_date_str} - {current_time}"

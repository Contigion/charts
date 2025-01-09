def candlestick_index_callback(context, component_text, n_candles):
    text = component_text.split(' ')
    prefix = text[0]
    index = int(text[1])

    triggered_id = context.triggered[0]['prop_id'].split('.')[0]

    if triggered_id == 'controls-decrease' and index > 0:
        return f'{prefix} {index - 1}'
    if triggered_id == 'controls-restart':
        return f'{prefix} {0}'
    if triggered_id == 'controls-increase' and n_candles is not None and (index + 1) < n_candles:
        return f'{prefix} {index + 1}'

    return component_text


def play_pause_callback(current_classes):
    if 'play' in current_classes:
        return current_classes.replace('play', 'pause').replace('green', 'yellow')

    if 'pause' in current_classes:
        return current_classes.replace('pause', 'play').replace('yellow', 'green')

    return current_classes

from dash import html


def button(button_id, text, class_name=''):
    classes = ' '.join(['component button', class_name])
    return html.Button(text, id=button_id, className=classes, n_clicks=0)

from dash.html import Button, I


def button(button_id, text, class_name=''):
    classes = ' '.join(['component button', class_name])
    return Button(text, id=button_id, className=classes, n_clicks=0)


def icon_button(icon_id, class_name):
    classes = ' '.join(['component icon icon-button', class_name])
    return I(className=classes, id=icon_id, n_clicks=0)

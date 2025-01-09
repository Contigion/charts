from dash.html import Button, I, P, Div
from dash_daq import BooleanSwitch


def button(button_id, text_input, class_name=''):
    classes = ' '.join(['component button', class_name])
    return Button(text_input, id=button_id, className=classes, n_clicks=0)


def icon_button(icon_id, class_name):
    classes = ' '.join(['component icon icon-button', class_name])
    return I(className=classes, id=icon_id, n_clicks=0)


def switch(switch_id, text_input, class_name=''):
    classes = ' '.join(['container container-row switch-container', class_name])
    switch_component = Div([
        P(id=f'{switch_id}-text', children=text_input, className='component text switch-text bold-text'),
        BooleanSwitch(id=switch_id, on=False, className='switch', color='#02203b')  # pylint: disable=not-callable
    ], className=classes)

    return switch_component

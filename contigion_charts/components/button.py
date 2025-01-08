from dash.html import Button, I
from dash_daq import BooleanSwitch
from .container import container_row
from .text import text


def button(button_id, text_input, class_name=''):
    classes = ' '.join(['component button', class_name])
    return Button(text_input, id=button_id, className=classes, n_clicks=0)


def icon_button(icon_id, class_name):
    classes = ' '.join(['component icon icon-button', class_name])
    return I(className=classes, id=icon_id, n_clicks=0)


def switch(switch_id, text_input, class_name=''):
    classes = ' '.join(['component switch-container', class_name])
    switch_component = container_row([
        text(f'{switch_id}-text', text_input, 'switch-text bold-text'),
        BooleanSwitch(id=switch_id, on=False, className='switch', color='#02203b')  # pylint: disable=not-callable
    ], class_name=classes)

    return switch_component

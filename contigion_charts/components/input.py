from dash.dcc import Dropdown
from dash.html import Div, P
from dash_bootstrap_components import Input


def dropdown(dropdown_id, label, default_value, options, className=''):
    classes = ' '.join(['component input', className])
    return Div([
        P(label, className='input-label'),
        Dropdown(
            id=dropdown_id,
            options=options,
            value=default_value,
            style={'color': '#000000'}
        )
    ], className=classes)


def number_input(input_id, label, default_value, step, minimum=0, className=''):
    classes = ' '.join(['component input', className])
    return Div([
        P(label, className='input-label'),
        Input(
            id=input_id,
            type='number',
            value=default_value,
            step=step,
            min=minimum,
            style={'color': '#000000'})
    ], className=classes)

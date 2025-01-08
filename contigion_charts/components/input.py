from dash.dcc import Dropdown, Checklist
from dash.html import Div, P
from dash_bootstrap_components import Input


def dropdown(dropdown_id, label, default_value, options, class_name=''):
    classes = ' '.join(['component input', class_name])
    return Div([
        P(label, className='input-label'),
        Dropdown(
            id=dropdown_id,
            options=options,
            value=default_value,
            style={'color': '#000000'}
        )
    ], className=classes)


def number_input(input_id, label, default_value, step, minimum=0, class_name=''):
    classes = ' '.join(['component input', class_name])
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


def checklist(checkbox_id, label, default_value, options, class_name=''):
    classes = ' '.join(['component input', class_name])
    return Div([
        P(label, className='input-label'),
        Checklist(
            id=checkbox_id,
            options=options,
            value=[default_value],
            style={'color': '#000000'},
            className='checklist'
        )
    ], className=classes)

from dash.dcc import Dropdown, Checklist, Upload
from dash.html import Div, P, A
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


def upload(upload_id, class_name='', file_type='CSV', allow_multiple=False):
    classes = ' '.join(['component upload', class_name])
    return Upload(
        id=upload_id,
        children=Div([
            Div([
                P('Drag and drop file or ', id=f'{upload_id}-label', className='component text'),
                A(f'Select a {file_type} file', id=f'{upload_id}-button', className='component text button')
            ], className='container container-row zero-padding-margin container-space-around'),
            P('No file uploaded.', id=f'{upload_id}-output', className='component text'),
        ], className='container container-col zero-padding-margin container-space-around'),
        multiple=allow_multiple,
        className=classes
    )

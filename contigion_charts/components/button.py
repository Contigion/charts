from dash import html


def button(button_id, text, className=''):
    classes = ' '.join(['component button', className])
    return html.Button(text, id=button_id, className=classes, n_clicks=0)

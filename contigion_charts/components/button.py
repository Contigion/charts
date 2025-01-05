from dash import html


def button(id, text, className='default-button'):
    return html.Button(text, id=id, className=className, n_clicks=0)

from dash.html import Div


def page(page_id, children=None, className=''):
    classes = ' '.join(['container page full-height full-width container-col', className])
    return Div(children, id=page_id, className=classes)


def background():
    return Div([], className="background")


def content_container_row(children=None, className=''):
    classes = ' '.join(['container content-container container-row', className])
    return Div(children, className=classes)


def content_container_col(children=None, className=''):
    classes = ' '.join(['container content-container container-col', className])
    return Div(children, className=classes)


def container_row(children=None, className=''):
    classes = ' '.join(['container container-row', className])
    return Div(children, className=classes)


def container_col(children=None, className=''):
    classes = ' '.join(['container container-col', className])
    return Div(children, className=classes)

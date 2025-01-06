from dash.html import Div


def page(children=None, className=''):
    classes = ' '.join(['container page', className])
    return Div(children, className=classes)


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

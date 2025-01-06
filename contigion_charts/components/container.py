from dash.html import Div


def page(page_id, children=None, class_name=''):
    classes = ' '.join(['container page full-height full-width container-col', class_name])
    return Div(children, id=page_id, className=classes)


def background():
    return Div([], className="background")


def container(children=None, class_name=''):
    classes = ' '.join(['container', class_name])
    return Div(children, className=classes)


def content_container_row(children=None, class_name=''):
    classes = ' '.join(['container content-container container-row', class_name])
    return Div(children, className=classes)


def content_container_col(children=None, class_name=''):
    classes = ' '.join(['container content-container container-col', class_name])
    return Div(children, className=classes)


def container_row(children=None, class_name=''):
    classes = ' '.join(['container container-row', class_name])
    return Div(children, className=classes)


def container_col(children=None, class_name=''):
    classes = ' '.join(['container container-col', class_name])
    return Div(children, className=classes)

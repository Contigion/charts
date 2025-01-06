from dash.html import H1, H2, H3, P, A, I


def title(title_id, text_input, class_name=''):
    classes = ' '.join(['component text', class_name])
    return H1(text_input, id=title_id, className=classes)


def heading(heading_id, text_input, class_name=''):
    classes = ' '.join(['component text', class_name])
    return H2(text_input, id=heading_id, className=classes)


def sub_heading(sub_heading_id, text_input, class_name=''):
    classes = ' '.join(['component text', class_name])
    return H3(text_input, id=sub_heading_id, className=classes)


def text(text_id, text_input, class_name=''):
    classes = ' '.join(['component text', class_name])
    return P(text_input, id=text_id, className=classes)


def link(link_id, text_input, href, class_name=''):
    classes = ' '.join(['component text', class_name])
    return A(text_input, href=href, id=link_id, className=classes)


def icon(icon_id, class_name):
    classes = ' '.join(['component icon', class_name])
    return I(className=classes, id=icon_id)

from dash.html import H1, H2, H3, P, A


def title(title_id, text_input, className=''):
    classes = ' '.join(['component text', className])
    return H1(text_input, id=title_id, className=classes)


def heading(heading_id, text_input, className=''):
    classes = ' '.join(['component text', className])
    return H2(text_input, id=heading_id, className=classes)


def sub_heading(sub_heading_id, text_input, className=''):
    classes = ' '.join(['component text', className])
    return H3(text_input, id=sub_heading_id, className=classes)


def text(text_id, text_input, className=''):
    classes = ' '.join(['component text', className])
    return P(text_input, id=text_id, className=classes)


def link(link_id, text_input, href, className=''):
    classes = ' '.join(['component text', className])
    return A(text_input, href=href, id=link_id, className=classes)

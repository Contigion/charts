from dash import register_page, callback, Output, Input, State, no_update
from dash.dcc import Store
from contigion_charts.components import page, title, content_container_row, container, container_col, container_row
from contigion_charts.components.graph import strategy_chart
from contigion_charts.components.input import upload
from contigion_charts.components.text import paragraph, icon, link
from contigion_charts.util.functions import parse_csv_data

register_page(__name__, path='/visualise', title='Contigion Charts', name='charts')


def layout():
    back_button = icon('test_to_home-icon', 'bi bi-arrow-left-circle-fill')

    page_title = container_col([
        title('page-title', 'Visualise your data', 'bold-text'),
        paragraph('page-description', [
            'Import your csv to visualise your data on a chart. Your data needs to have the following columns: ',
            'time, open, high, low, close, '
            'point_y (for points) or line_y (for a continuous line) or signal (for Buy and Sell labelled points).'
        ])
    ], class_name='fit-content zero-padding-margin')

    page_title_container = content_container_row([
        container_row([
            link(f'{back_button.id}-container', back_button, '/'),
            page_title
        ], class_name='fit-content zero-padding-margin'),

        upload('add-data-upload')
    ], class_name='container-space-between')

    chart_container = container(class_name='graph-container')
    chart_container.id = 'visualise-chart-container'

    test_page = page(page_id='visualise-page', children=[
        page_title_container,
        chart_container,
        Store(id='store-data', storage_type='local')
    ])

    return test_page


@callback(
    [
        Output('add-data-upload-output', 'children'),
        Output('visualise-chart-container', 'children'),
        Output('store-data', 'data'),
    ],
    Input('add-data-upload', 'contents'),
    State('add-data-upload', 'filename'),
    prevent_initial_call=True
)
def update_output(content, filename):
    if content is not None and filename.endswith('csv'):
        data = parse_csv_data(content)
        chart = strategy_chart(data)
        return filename, chart, content

    return no_update, no_update, no_update

import dash
import dash_core_components as dcc
import dash_html_components as html
import json
from dash.dependencies import Input, Output
from textwrap import dedent as d

app = dash.Dash(__name__)
styles = {'pre': {'border': 'thin lightgrey solid', 'overflowX': 'scroll'}}
app.layout = html.Div([
    dcc.Graph(id='basic-interactions',
              figure={'data': [{'x': [1, 2, 3, 4],
                                'y': [4, 1, 3, 5],
                                'text': ['a', 'b', 'c', 'd'],
                                'customdata': ['c.a', 'c.b', 'c.c', 'c.d'],
                                'name': 'Trace1',
                                'mode': 'markers',
                                'marker': {'size': 12}},
                               {'x': [1, 2, 3, 4],
                                'y': [9, 4, 1, 4],
                                'customdata': ['c.w', 'c.x', 'c.y', 'c.z'],
                                'name': 'Trace2',
                                'mode': 'markers',
                                'marker': {'size': 12}}]}),
    html.Div(
        className='row',
        children=[
            html.Div(
                [dcc.Markdown(d(
                    '''
                    ** Hover Data **

                    Mouse over values in the graph.''')),
                 html.Pre(id='hover-data', style=styles['pre'])],
                className='three columns'),
            html.Div(
                [dcc.Markdown(d(
                    '''
                    ** Click Data **

                    Click on points in the graph.''')),
                 html.Pre(id='click-data', style=styles['pre'])],
                className='three columns'),
            html.Div(
                [dcc.Markdown(d(
                    '''
                    ** Selection Data **

                    Choose the lasso or rectangle tool in the graph's 
                    bar and then select points in the graph.''')),
                 html.Pre(id='selected-data', style=styles['pre'])],
                className='three columns'),
            html.Div(
                [dcc.Markdown(d(
                    '''
                    ** Zoom and Relayout Data **

                    Click and drag on the graph to zoom, or click on the zoom
                    buttons in the graph's menu bar.
                    Clicking on the legend items will also fire this 
                    event.''')),
                 html.Pre(id='relayout-data', style=styles['pre'])],
                className='three columns')])
])
                 

@app.callback(Output('hover-data', 'children'),
              [Input('basic-interactions', 'hoverData')])
def display_hover_data(data):
    return json.dumps(data, indent=2)


@app.callback(Output('click-data', 'children'),
              [Input('basic-interactions', 'clickData')])
def display_click_data(data):
    return json.dumps(data, indent=2)


@app.callback(Output('selected-data', 'children'),
              [Input('basic-interactions', 'selectedData')])
def display_selected_data(selected_data):
    return json.dumps(selected_data, indent=2)


@app.callback(Output('relayout-data', 'children'),
              [Input('basic-interactions', 'relayoutData')])
def display_selected_data(relayout_data):
    return json.dumps(relayout_data, indent=2)



if __name__ == '__main__':
    app.run_server(debug=True)

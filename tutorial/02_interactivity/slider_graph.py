#!/user/bin/env python3

import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go

df = pd.read_csv(
    'https://raw.githubusercontent.com/plotly/'
    'datasets/master/gapminderDataFiveYear.csv')
app = dash.Dash()

app.layout = html.Div([
    dcc.Graph(id='graph-with-slider'),
    dcc.Slider(
        id='year-slider',
        min=df.year.min(),
        max=df.year.max(),
        value=df.year.min(),
        step=None,
        marks={str(year): str(year) for year in df.year.unique()})])

@app.callback(
    dash.dependencies.Output('graph-with-slider', 'figure'),
    [dash.dependencies.Input('year-slider', 'value')])
def update_figure(selected_year):
    subset = df[df.year == selected_year]
    traces = []

    for i in subset.continent.unique():
        continent_df = subset[subset.continent == i]
        traces.append(go.Scatter(
            x=continent_df.gdpPercap,
            y=continent_df.lifeExp,
            text=continent_df.country,
            mode='markers',
            opacity=0.7,
            marker={'size': 15, 'line': {'width': 0.5, 'color': 'white'}},
            name=i))
    return {'data': traces,
            'layout': go.Layout(
                xaxis={'type': 'log', 'title': 'GDP Per Capita'},
                yaxis={'title': 'Life Expectancy', 'range': [20, 90]},
                margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                legend={'x': 0, 'y': 1},
                hovermode='closest')}

if __name__ == '__main__':
    app.run_server()
    

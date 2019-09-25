# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bio as dashbio
import plotly.plotly as py
import plotly.graph_objs as go
import pandas as pd
import numpy as np

app = dash.Dash()
server = app.server
df = pd.read_csv(
    'https://raw.githubusercontent.com/LeoMonrroy/legendary-palm-tree/master/'
)

app.layout = html.Div(children=[
    html.H1(children='Försök till visualiseing'),
    html.Div(children='''
        Grupp 6
    '''),
    dcc.Graph(
        id='Försök till datavisualisering',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'line', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'line', 'name': u'Montréal'},
            ],
            'layout': {
                'title': 'Dash Data Visualization'
            }
        }
    ),
    dcc.Input(id='my-id', value='initial value', type="text"),
    html.Div(id='my-div')
])


@app.callback(
    Output(component_id='my-div', component_property='children'),
    [Input(component_id='my-id', component_property='value')]
)
def update_output_div(input_value):
    return 'You\'ve entered "{}"'.format(input_value)

# -*- coding: utf-8 -*-

import dash
import dash_core_components as dcc
import dash_html_components as html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

colors = {
    'background' : "#111111",
    'text' : '#7FDBFF'
}

def generate_generic_graph(data, id, title):
    return dcc.Graph(
        id=id, 
        figure={
            'data': data,
            'layout': {
                'title': title,
                'plot_bgcolor' : colors['background'], 
                'paper_bgcolor' : colors['background'],
                'font' : {
                    'color' : colors['text']
                }
            }
        }
    )

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(children='STEM Local Atmosphere Monitor (SLAM)', style={
        'textAlign' : 'center', 
        'color' : colors['text']
    }), 

    html.Div(children=[
        html.H2(children="")
        ], style={
        'textAlign' : 'center', 
        'color' : colors['text']
    }),

    generate_generic_graph([
        {'y' : [0.5, 2.4, 1.4, 1, 3, 2, 1], 'type' : 'scatter', 'name' : 'Upload Speed'}, 
        {'y' : [0.6, 2.6, 1.2, 0.6, 2, 1, 0.1], 'type' : 'line', 'name' : "Download Speed"}
    ], "test-generate2", "I also hope this works"),

    generate_generic_graph([
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
            ], "test-generate", "I hope this works"),

    dcc.Graph(
        id="example-graph2",
        figure={
            'data': [
                {'x': [1, 2, 4], 'y': [4, 1, 2], 'type': 'bar', 'name': 'Vancouver'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': 'Winnipeg'},
            ],
            'layout': {
                'title': 'So are these!',
                'plot_bgcolor' : colors['background'], 
                'paper_bgcolor' : colors['background'],
                'font' : {
                    'color' : colors['text']
                }
            }
        }
    )

])

if __name__ == '__main__':
    app.run_server(debug=True)
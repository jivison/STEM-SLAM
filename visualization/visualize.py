# -*- coding: utf-8 -*-

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

import pandas as pd

database_file = "../data/database.csv"
df = pd.read_csv(database_file).tail(7)

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

colors = {
    'background' : "#111111",
    'text' : '#7FDBFF'
}

def generate_graph_from_data_frame(dataframe, id, title, desired_data_types):
    
    data = []

    for data_type in desired_data_types:
        data.append(go.Scatter(
            {'y' : dataframe[data_type]}
        ))

    return dcc.Graph(
        id=id,
        figure={
            'data' : data,
            'layout': {
                'title': title,
                'plot_bgcolor' : colors['background'], 
                'paper_bgcolor' : colors['background'],
                'font' : {
                    'color' : colors['text']
                },
                'xaxis' : dict(title="Minutes since last scan")
            }
        }
    )

def generate_graph_from_raw_data(data, id, title):
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

    generate_graph_from_data_frame(df, "particles", "Methane, CO2, and Radon Levels", [
        "methane_levels", "radon_levels", "c02_levels"
        ]),

    generate_graph_from_data_frame(df, "network", "Upload and Download Speeds", [
        "download_speed", "upload_speed"
    ])

])

if __name__ == '__main__':
    app.run_server(debug=True)
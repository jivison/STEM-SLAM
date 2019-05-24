#!/bin/python
# -*- coding: utf-8 -*

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd

import pandas as pd

# My custom themes. Feel free to add more if you would like
import custom_themes as themes

t = themes.Themes()

# Time that continuous.sh waits between scans

interval = 300
minute_interval = interval / 60

display_period = 5 

# Number of x values on a graph
number_of_entries = 100

def create_x_list():
    output = []
    for x in range(number_of_entries):
        output.append(x * minute_interval)
    return output

def average(array):
    average = sum(array)/len(array)
    return [average for x in range(number_of_entries)]

# Generates graph from a data frame
def generate_graph_from_data_frame(dataframe, raw_dataframe, id, title, desired_data_types, series_options, yaxis_title, xaxis_title):
    
    data = []

    # Plot each data_type called
    for data_type in desired_data_types:

        # Check for average data_types
        if "average" not in data_type:

            # Plot values newest first
            y_values = dataframe[data_type][::-1]
        else:
            # a_data_type extracts the actual data_type from the average
            a_data_type = data_type.partition("|")[2]
            y_values = average(raw_dataframe[a_data_type][:-number_of_entries:-1])

        data.append(go.Scatter(
            {'y' : y_values, 
            'x' : create_x_list(), 
            'name' : series_options[data_type]["series_name"],
            'line' : {
                'color' : series_options[data_type]['color'],
                'shape' : 'spline'
            }
            },
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
                    'color' : colors['text'],
                    'size' : 25
                },
                'height' : 700,
                'xaxis' : dict(title=xaxis_title, autorange="reversed", automargin=True),
                'yaxis' : dict(title=yaxis_title, automargin=True)
            }
        }
    )


database_file = "/home/stem-server/STEM-SLAM/server_files/data/database.csv"

# df is the raw_df with the last n number of values
# raw_df is used to calculate the average
raw_df = pd.read_csv(database_file)
df = raw_df.tail(number_of_entries)

external_stylesheets = [
    {
        'href' : 'visualize.css',
        'rel' : 'stylesheet',
        'crossorigin' : 'anonymous'
    }
]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# Initialize the server
server = app.server

colors = {
    'background' : "black",
    'text' : 'white'
}

DISPLAYARRAY = [
    generate_graph_from_data_frame(df, raw_df, "upload_speed", "Upload Speed", 
    ["upload_speed", "average|upload_speed"],
    {
            "upload_speed" : {
                "series_name" : "Upload Speed",
                "color" : t("vaporwave")[0]
            },
            "average|upload_speed" : {
                "series_name" : "Average Upload Speed",
                "color" : t("vaporwave")[1]
            }
        },
        "Speed (mbps)",
        "Time since last scan (minutes)"
    ), # End graph

    generate_graph_from_data_frame(df, raw_df, "download_speed", "Download Speed", 
    ["download_speed", "average|download_speed"],
    {
            "download_speed" : {
                "series_name" : "Download Speed",
                "color" : t("vaporwave")[5]
            },
            "average|download_speed" : {
                "series_name" : "Average Download Speed",
                "color" : t("vaporwave")[0]
            }
        },
        "Speed (mbps)",
        "Time since last scan (minutes)"
    ), # End graph

    generate_graph_from_data_frame(df, raw_df, "device_count", "Device Count", 
    ["device_count", "average|device_count"],
    {
            "device_count" : {
                "series_name" : "Number of Devices Connected to Network",
                "color" : t("vaporwave")[2]
            },
            "average|device_count" : {
                "series_name" : "Average Number of Devices Connected to Network",
                "color" : t("vaporwave")[3]
            }
        },
        "# of Devices",
        "Time since last scan (minutes)"
    ), # End graph

    generate_graph_from_data_frame(df, raw_df, "avg_ping", "Ping to 8.8.8.8",
    ['avg_ping', "average|avg_ping"],
    {
            "avg_ping" : {
                "series_name" : "Ping",
                "color" : t('vaporwave')[4]
            },
            "average|avg_ping" : {
                "series_name" : "Average Ping",
                "color" : t('vaporwave')[0]
            }
    },
    "Latency (ms)",
    "Time since last scan (minutes)"
    ), # End graph

    generate_graph_from_data_frame(df, raw_df, "smoke_levels", "Smoke Levels", 
    ["smoke_levels", "average|smoke_levels"],
    {
        "smoke_levels" : {
            "series_name" : "Smoke Levels",
            "color" : t('vaporwave')[1]
        },

        "average|smoke_levels" : {
            "series_name" : "Average Smoke Levels",
            "color" : t('vaporwave')[2]
        },
    },
        "Concentration (ppm)",
        "Time since last scan (minutes)"
    ), # End graph

    generate_graph_from_data_frame(df, raw_df, "combustable_gas_levels", "Combustable Gas Levels", 
    ["combustable_gas_levels", "average|combustable_gas_levels"],
    {
        "combustable_gas_levels" : {
            "series_name" : "Combustable Gas Levels",
            "color" : t('vaporwave')[3]
        },
        "average|combustable_gas_levels" : {
            "series_name" : "Average Combustable Gas Levels",
            "color" : t('vaporwave')[4]
        },
    },
        "Concentration (ppm)",
        "Time since last scan (minutes)"
    )
]

# The html framework
app.layout = html.Div([
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


    # This is what cycles through the graphs in DISPLAY_ARRAY
    html.Section(id="slideshow", children=[
        html.Div(id="slideshow-container", children=[
            html.Div(id="image"),
            dcc.Interval(id='interval', interval=15000)
        ])
    ])

])


# ?????
@app.callback(Output('image', 'children'),
              [Input('interval', 'n_intervals')])

# Returns the correct graph
def display_image(n):
    if n == None:
        n = 6

    return DISPLAYARRAY[n % 6]

if __name__ == '__main__':
    app.run_server(debug=True)



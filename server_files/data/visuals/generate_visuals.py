# -*- coding: utf-8 -*

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

import pandas as pd

# My custom themes. Feel free to add more if you would like
import custom_themes as themes

t = themes.Themes()

# Time that continuous.sh waits between scans

interval = 600
minute_interval = interval / 60


# Number of x values on a graph
number_of_entries = 16

def create_x_list():
    output = []
    for x in range(number_of_entries):
        output.append(x * minute_interval)
    return output


database_file = "/home/mattecatte/STEM-SLAM/server_files/data/database.csv"
df = pd.read_csv(database_file).tail(number_of_entries)

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css',
    {
        'href' : 'visualize.css',
        'rel' : 'stylesheet',
        'crossorigin' : 'anonymous'
    }
]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

colors = {
    'background' : "black",
    'text' : 'white'
}

def generate_graph_from_data_frame(dataframe, id, title, desired_data_types, series_options, yaxis_title, xaxis_title):
    
    data = []

    for data_type in desired_data_types:
        data.append(go.Scatter(
            {'y' : dataframe[data_type][::-1], 
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
                    'color' : colors['text']
                },
                'xaxis' : dict(title=xaxis_title, autorange="reversed"),
                'yaxis' : dict(title=yaxis_title)
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

    generate_graph_from_data_frame(df, "upload_speed", "Upload Speed", 
    ["upload_speed"],
    {
            "upload_speed" : {
                "series_name" : "Upload Speed",
                "color" : t("vaporwave")[0]
            }
        },
        "Speed (mbps)",
        "Time since last scan (minutes)"
    ), # End graph

    generate_graph_from_data_frame(df, "download_speed", "Download Speed", 
    ["download_speed"],
    {
            "download_speed" : {
                "series_name" : "Download Speed",
                "color" : t("vaporwave")[5]
            }
        },
        "Speed (mbps)",
        "Time since last scan (minutes)"
    ), # End graph

    generate_graph_from_data_frame(df, "device_count", "Device Count", 
    ["device_count"],
    {
            "device_count" : {
                "series_name" : "Number of Devices Connected to Network",
                "color" : t("vaporwave")[2]
            }
        },
        "# of Devices",
        "Time since last scan (minutes)"
    ), # End graph

    generate_graph_from_data_frame(df, "avg_ping", "Average ping to 8.8.8.8",
    ['avg_ping'],
    {
            "avg_ping" : {
                "series_name" : "Average Ping",
                "color" : t('vaporwave')[4]
            }
    },
    "Latency (ms)",
    "Time since last scan (minutes)"
    ), # End graph

    generate_graph_from_data_frame(df, "CO_levels", "Carbon Monoxide Levels", 
    ["CO_levels"],
    {
        "CO_levels" : {
            "series_name" : "Carbon Monoxide Levels",
            "color" : t('vaporwave')[1]
        },
    },
        "Concentration (ppm)",
        "Time since last scan (minutes)"
    ), # End graph

    generate_graph_from_data_frame(df, "methane_levels", "Methane Levels", 
    ["methane_levels"],
    {
        "methane_levels" : {
            "series_name" : "Methane Levels",
            "color" : t('vaporwave')[3]
        },
    },
        "Concentration (ppm)",
        "Time since last scan (minutes)"
    )

    # Sample graph (copypasta)
    # generate_graph_from_data_frame(<dataframe>, "<graph ID>", "<graph title>", 
    # ["<data_type1>", "<data_type2>", ......."<data_typen>"],
    # {
    #         "<data_type1>" : {
    #             "series_name" : "<series name>",
    #             "color" : "<color>""
    #         },
    #         "<data_type2" : {
    #             "series_name" : "<series name>"
    #             "color" : "<color>"
    #         }
    #     },
    #     "<y axis title>",
    #     "<x axis title>"
    #     ), # End graph




    ])

if __name__ == '__main__':
    app.run_server(debug=True)


import base64
import datetime
import io

import dash
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html
import dash_table_experiments as dt

import plotly.plotly as py
import plotly.graph_objs as go
import plotly.figure_factory as FF

import numpy as np

import pandas as pd


df = pd.read_csv('networkdetails.csv')

sample_data_table = FF.create_table(df.head())

fig = ""

def graph_it(graph_x, graph_y_list, title, bg_color='rgb(230, 230, 230)'):
        trace_dict = {}
        for graph_y in graph_y_list:
            current_trace = "trace_{}".format(graph_y)
            trace_dict[current_trace] = go.Scatter(x=df[graph_x], y=df[graph_y], mode="lines", name=graph_y)
            layout = go.Layout(title=title, plot_bgcolor=bg_color)

        print(list(trace_dict.values()))
        fig = go.Figure(data=list(trace_dict.values()), layout=layout)

# Plot data in browser
graph_it("TIME", ["AVG PING TIME", "HOST PING TIME"], "Ping latency over time")
py.plot(fig, filename='simple-plot-from-csv')
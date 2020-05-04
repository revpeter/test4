import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import numpy as np

#Fajl beolvasas
hh = pd.read_csv("heart.csv")
hh["sex2"] = hh["sex"].replace({1:"F", 0:"N"})

#Stilusok
s1 = {"color": "black",
      "font-weight": "bold",
      "text-align": "center",
      'backgroundColor': 'rgb(250, 250, 250)',
      "display": "inline-block",
      "width": "50%"}

s2 = {"color": "blue",
      "text-align": "center",
      "display": "inline-block",
      "width": "100%"}

#Dropdown values
optionsM = []
for i in hh.columns:
    optionsM.append({'label': i, 'value': i})

#App
app = dash.Dash(__name__)
server = app.server
app.title="Test4"

app.layout = html.Div(children = [html.Div("WELCOMME", style = s2),
                                  html.Div(html.Label(["y-tengely",
                                                       dcc.Dropdown(id = "drop_down1",options = optionsM, value = "chol")]),
                                           style = s1),
                                  html.Div(html.Label(["x-tengely",
                                                       dcc.Dropdown(id = "drop_down2",options = optionsM, value = "age")]),
                                           style = s1),
                                  html.Div(dcc.Markdown("""Az y-tengely arra jo hogy..."""), style = s1),
                                  html.Div(dcc.Markdown("""Az x-tengely arra jo hogy..."""), style = s1),
                                  html.Div(children = [dcc.Graph(id = "plot_area")],
                                           style = s2)])


@app.callback(Output("plot_area", "figure"), [Input("drop_down1", "value"), Input("drop_down2", "value")])

def updateplot(ff_val, ff_x):
    fig = px.scatter(hh, x=ff_x, y=ff_val, 
                 color='sex2', color_discrete_map= {"1": 'blue', "0": 'green'})
    return({"data": fig.data, "layout":fig.layout})

if __name__ == "__main__":
    app.run_server()

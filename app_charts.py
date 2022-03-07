import dash
from dash import  dcc, html, Input, Output

import dash_bootstrap_components as dbc
import altair as alt
from vega_datasets import data

cars = data.cars()

# def plot_altair(xcol,xmax):
#     #print(xmax)
#     chart = alt.Chart(cars[cars['Horsepower']<xmax]).mark_point().encode(
#         x=xcol,
#         y='Weight_in_lbs')
#     return chart.interactive().to_html()

app = dash.Dash(__name__)
server = app.server
app.layout = html.Div([
        dcc.Dropdown(
            id='xcol', value='Horsepower',
            options=[{'label': i, 'value': i} for i in cars.columns]),
        html.Iframe(
        id="xscatter",
        #srcDoc=plot_altair(xmax=200,xcol='Horsepower'),
        style={'border-width': '0', 'width': '100%', 'height': '400px'}),
        dcc.Slider(id="xslider",min=0,max=240)               
    ])


@app.callback(
    Output("xscatter",'srcDoc'),
    Input('xcol','value')
    
)
def plot_altair(xcol):
    #print(xmax)
    chart = alt.Chart(cars).mark_point().encode(
        x=xcol,
        y='Weight_in_lbs')
    return chart.interactive().to_html()

if __name__ == '__main__':
    app.run_server(debug=True,host="127.0.0.3") 
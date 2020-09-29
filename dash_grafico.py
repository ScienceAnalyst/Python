import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd

datos = pd.read_csv('/Users/Yomero/Documents/Proyecto_Py/ligamx2010_atlas.csv', skiprows=6,encoding="utf-8")
atlas2010 = datos.dropna(subset=['Edad'])
#atlas2010.head()

caracteristicas = atlas2010.columns

app = dash.Dash()

app.layout = html.Div([
            html.Div([
            dcc.Dropdown(id='selector1',
                         options=[{'label':i, 'value':i} for i in caracteristicas], 
                         value='Jugador')
            ], style={'width':'48%', 'display':'inline-block'}),
            
            html.Div([
            dcc.Dropdown(id='selector2',
                         options=[{'label':i, 'value':i} for i in caracteristicas], 
                         value='Posc')
            ], style={'width':'48%', 'display':'inline-block'}),
        
            dcc.Graph(id='grafico')
], style={'padding':14})
    
@app.callback(Output('grafico','figure'),
            [Input('selector1','value'),
             Input('selector2','value')])

def actulizar(valor_selector1, valor_selector2):
    return{
        'data':[go.Scatter(x=atlas2010[valor_selector1],
                                 y=atlas2010[valor_selector2],
                                 text=atlas2010['Jugador'],
                                 mode='markers',
                                 marker={'size':14, 'opacity':0.6}
                               )],
        'layout':go.Layout(title='Grafico de Jugadores según sus características',
                          xaxis={'title':valor_selector1},
                          yaxis={'title':valor_selector2}, 
                          )        
    }
app.run_server()
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from dash.dependencies import Input, Output, State

myheading1 = 'Risk Assessment Tool'
q_1='What is the likelihood of coup or extra-constitutional change?'

responses=[1,2,3,4,5]

app.layout = html.Div(children=[
    html.H1(myheading1),
    html.Div([
            html.H6(q_1),
            dcc.Dropdown(
                id='pick_score_q1',
                options=[
                        {'label':responses[0], 'value':responses[0]},
                        {'label':responses[1], 'value':responses[1]},
                        {'label':responses[2], 'value':responses[2]},
                        {'label':responses[3], 'value':responses[3]},
                        {'label':responses[4], 'value':responses[4]},
                        ],
                value='',
                ),
        ]

@app.callback(Output('your_output_here', 'children'),
              [Input('pick_score_q1', 'value')]),
html.H2(pick_score_q1)


if __name__ == '__main__':
    app.run_server()

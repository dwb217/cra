import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from dash.dependencies import Input, Output, State

myheading1 = 'Risk Assessment Tool'
q_1='What is the likelihood of coup or extra-constitutional change?'
q_2='How legitimate is the government?'
q_3='How significant is wealth disparity in the country?'
q_4='How great a risk is terrorism?'
q_5='Are foreign companies and/or individuals are particular risk?'

note='1 is low or strong no; 5 is high or strong yes.'

responses=[1,2,3,4,5]

def calc(pick_score_q1,pick_score_q2,pick_score_q3):
    score = 0
    for x in score:
        score +=x/len(args)
    return score

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
            html.H6(q_1),
            dcc.Dropdown(
                id='pick_score_q2',
                options=[
                        {'label':responses[0], 'value':responses[0]},
                        {'label':responses[1], 'value':responses[1]},
                        {'label':responses[2], 'value':responses[2]},
                        {'label':responses[3], 'value':responses[3]},
                        {'label':responses[4], 'value':responses[4]},
                        ],
                value='',
                ),
            html.H6(q_1),
            dcc.Dropdown(
                id='pick_score_q3',
                options=[
                        {'label':responses[0], 'value':responses[0]},
                        {'label':responses[1], 'value':responses[1]},
                        {'label':responses[2], 'value':responses[2]},
                        {'label':responses[3], 'value':responses[3]},
                        {'label':responses[4], 'value':responses[4]},
                        ],
                value='',
                )
        ]

@app.callback(Output('your_output_here', 'children'),
              [Input('pick_score_q1', 'value')]),
html.H2(score)



if __name__ == '__main__':
    app.run_server()

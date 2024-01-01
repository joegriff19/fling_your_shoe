from app import app, server  # NEED THE IMPORT SERVER FOR RENDER
from dash import dcc, html, clientside_callback, State, ctx
import dash
import dash_bootstrap_components as dbc
from dash.dependencies import Output, Input
import os
from flask import send_from_directory
import dash_extensions as de

options = dict(loop=True, autoplay=True, rendererSettings=dict(preserveAspectRatio='xMidYMid slice'))

dash.register_page(__name__)

# padding for the page content
CONTENT_STYLE = {
    "margin-left": "2rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

# Index Page Layout
colors = {
    # 'background': '#ffffff',
    'text': '#0000CD'
}

content = html.Div(id="page-content", children=[], style=CONTENT_STYLE)

# define layout
app.layout = html.Div([
    dcc.Location(id="url"),
    content,
])


game_layout = html.Div(
    children=[
        html.Header(
            children=[
                # html.Div(dls.Hash(fullscreen=True), style={"height": "200px"}),
                html.Div([
                    html.Div("GO !", className="title"),
                    html.Br(),
                    dcc.Interval(id='game_time', interval=5000, n_intervals=0, max_intervals=1),
                    dbc.Button(id='shoe_clicks', size="lg",
                               n_clicks=0, className="shoe_button",
                               style={
                                    'background-color': '#2dbecd',
                                    'color': '#ffc832',
                                }),
                    # html.Button(id='shoe_clicks', n_clicks=0, className="shoe_button"),
                    html.Div(id='shoe_clicks_output', className="title"),
                    html.Div(id='time_up', className="title")
                ],
                    style={
                        'textAlign': 'center',
                        'color': 'black',
                        'max-width': '500px',
                        'margin': 'auto'
                    }),
                html.Div(children=" "),

            ]
        )
        ]
)


# @app.callback(
#     Output('shoe_clicks_output', 'children'),
#     Input('shoe_clicks', 'n_clicks'),
#     Input('game_time', 'n_intervals'),
#     prevent_initial_call=True
# )
# def display_click(n_clicks):
#     final_score = n_clicks
#     # self.final_score = n_clicks
#     return final_score


@app.callback(
    Output('time_up', 'children'),
    Input('game_time', 'n_intervals'),
    Input('shoe_clicks', 'n_clicks'),
    prevent_initial_call=True
)
def end_game(n_intervals, n_clicks):
    global final_score
    if n_intervals == 0:
        final_score = n_clicks
        return final_score

    if n_intervals == 1:
        # final_score = n_clicks
        # final_score_print = final_score
        # final_score = 0
        return (html.Div("time is up!"),
                html.Div(de.Lottie(options=options, width="10vh", height="10vh", url="/loader", speed=1,
                                   isClickToPauseDisabled=True),
                         # style={'display': 'inline-block', "position": "absolute", "top": "55px"}
                         ),
                html.Div(f"your shoe flew {final_score} feet!"),
                dbc.Button(children='play again', id='home',
                           # href=dash.page_registry['index']['path']))
                           href='/'))

    # elif game_time == 2:
    #     return (html.Div("click the button below to see how far you flung your shoe"),
    #            dbc.Button(children='watch my shoe fling', id='fling_results',
    #                       href=dash.page_registry['pages.game_over']['path']))


@server.route("/loader", methods=['GET'])
def serving_lottie_loader():
    directory = os.path.join(os.getcwd(), "assets/lottie")
    return send_from_directory(directory, "shoe.json")
# Import Packages and other files for app
# import index
from app import app, server  # NEED THE IMPORT SERVER FOR RENDER
import dash
from dash import dcc, html, clientside_callback, State, ctx
import dash_bootstrap_components as dbc
from dash.dependencies import Output, Input
from pages import game
# import time
# import requests
# from bs4 import BeautifulSoup
# import pandas as pd
# import lxml
# import warnings
# from datetime import date
# import time
# import dash_player as dp
# import dash_leaflet as dl
# import coordinates
# import globe
# import weather
# import city_list
# import dash_mantine_components as dmc
# from dash_iconify import DashIconify
# import dash_extensions as de
# import os
# from flask import send_from_directory
# import dash_loading_spinners as dls

# from pages.game import game_layout
# from pages.game_over import game_over_layout

dash.register_page(__name__)

# today = date.today()
# warnings.simplefilter(action='ignore', category=FutureWarning)

# GITHUB = 'https://github.com/joegriff19'
# LINKEDIN = 'https://www.linkedin.com/in/joseph-m-griffin/'
# VENMO = 'https://venmo.com/u/joegriff19'
# LOTTIE = 'https://assets5.lottiefiles.com/packages/lf20_GoeyCV7pi2.json'
# LOTTIE = 'https://assets2.lottiefiles.com/packages/lf20_mDnmhAgZkb.json'
# options = dict(loop=True, autoplay=True, rendererSettings=dict(preserveAspectRatio='xMidYMid slice'))

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
# index page layout
index_layout = html.Div(
    children=[
        html.Header(
            children=[
                # html.Div(dls.Hash(fullscreen=True), style={"height": "200px"}),
                html.Div([
                    html.Div("How Far Can You Fling Your Shoe?", className="title"),
                    html.Br(),
                    html.Div("Select your shoe of choice"),
                    dcc.Dropdown(['👟', '👠', '👞', '🥾', '👢', '🥿', '👡', '🩰','🩴', '⛸️', '🧦', '🦶🏼'],
                                 clearable=False, searchable=False, id='shoe_dropdown'),
                    html.Div(id='shoe_dropdown_output'),
                    html.Br(),
                    # html.Div("the more times you click the button, the farther you fling your shoe!"),
                    html.Br(),
                    # html.Div(id='ready_clicks_output', className="title"),
                    # html.Div(id='shoe_clicks_output', className="title")

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


@app.callback(
    Output('shoe_dropdown_output', 'children'),
    Input('shoe_dropdown', 'value'),
    prevent_initial_call=True
)
def update_output(value):
    global chosen_shoe
    chosen_shoe = value
    return (html.Br(),
            html.Div(f'You have selected {value}'),
            html.Br(),
            html.Div("a 'shoe flinging power' button will appear on the next page"),
            html.Br(),
            html.Div("the more times you click the button, the farther you fling your shoe!"),
            html.Br(),
            html.Div("when you are ready to play, click the 'ready to fling' button below!"),
            html.Br(),
            dbc.Button(children='ready to fling', id='ready_button', href=dash.page_registry['pages.game']['path'])
            # html.Button('ready to fling', id='ready_clicks', n_clicks=0, className="shoe_button"),
            )


@app.callback(
    Output('ready_clicks_output', 'children'),
    Input('ready_clicks', 'n_clicks'),
    prevent_initial_call=True
)
def show_flinging_power_button(ready_clicks):
    if ready_clicks > 0:
        return html.Button('shoe flinging power', id='shoe_clicks', n_clicks=0, className="shoe_button"),


# @app.callback(
#     Output('shoe_clicks_output', 'children'),
#     Input('shoe_clicks', 'n_clicks'),
#     prevent_initial_call=True
# )
# def display_click(btn):
#     if "shoe_clicks" == ctx.triggered_id:
#         msg = "Shoe button was clicked"
#     return btn


@app.callback(
    Output('page-content', 'children', ),
    [Input('url', 'pathname', )]
)
def render_page_content(pathname):
    if pathname == '/':
        return index_layout
    elif pathname == '/index':
        return index_layout
    elif pathname == '/game':
        return game.game_layout

    # below pathname with /pages needed for render app
    elif pathname == '/pages/index':
        return index_layout
    elif pathname == 'pages/game':
        return game.game_layout

    # elif pathname == '/game-over':
    #     return game_over_layout
    # If the user tries to reach a different page, return a 404 message
    else:
        return dbc.Container(
            [
                html.H1("404: Page not found", className="text-danger"),
                html.P(
                    "Please return to the home page",
                    className="lead",
                )])

# def show_game():
#     pass
#
#
# def recent_form():
#     pass
#
#
# def show_table():
#     pass



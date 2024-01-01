from app import app, server  # NEED THE IMPORT SERVER FOR RENDER
from dash import dcc, html, clientside_callback, State, ctx
import dash
# from pages.game import final_score

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


game_over_layout = html.Div(
    children=[
        html.Header(
            children=[
                # html.Div(dls.Hash(fullscreen=True), style={"height": "200px"}),
                html.Div([
                    html.Div("How Far Game Over Page", className="title"),
                    # html.Br(),
                    # html.Div(f"Final score is {pages.game.final_score}"),
                    # dcc.Dropdown(['👟', '👠', '👞', '🥾', '👢', '🥿', '👡', '🩰','🩴', '⛸️', '🧦', '🦶🏼'],
                    #              clearable=False, searchable=False, id='shoe_dropdown'),
                    # html.Div(id='shoe_dropdown_output'),
                    # html.Br(),
                    # # html.Div("the more times you click the button, the farther you fling your shoe!"),
                    # html.Br(),
                    # # html.Button('shoe flinging power', id='btn-nclicks', n_clicks=0, className="shoe_button"),
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
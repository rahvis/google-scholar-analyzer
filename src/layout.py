import dash
from dash import dcc, html

def create_layout():
    """
    Create the layout for the Dash application.

    Returns:
    - html.Div: The Dash layout with author rankings graph and details section.
    """
    return html.Div([
        html.H1("Author Rankings", style={'textAlign': 'center'}),
        dcc.Graph(id="graph"),
        html.Div(id="author-details", style={"marginTop": "20px", "padding": "10px"})
    ])

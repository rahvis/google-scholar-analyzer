from dash import Input, Output
from graph_builder import generate_graph_figure
from ranking_calculator import generate_rankings

def register_callbacks(app, authors_data):
    """
    Register Dash app callbacks for updating the graph and displaying author details.

    Args:
    - app (Dash): The Dash app instance.
    - authors_data (list): List of authors' data with rankings and scores.
    """
    rankings = generate_rankings(authors_data)
    
    @app.callback(
        [Output("graph", "figure"), Output("author-details", "children")],
        [Input("graph", "clickData")]
    )
    def update_graph(click_data):
        clicked_author = None
        if click_data:
            clicked_author = click_data["points"][0]["text"]
        
        # Generate graph figure
        fig = generate_graph_figure(rankings, clicked_author)

        # Display details for clicked author
        author_details = ""
        if clicked_author:
            author = next(a for a in rankings if a["name"] == clicked_author)
            metrics = {
                "Rank": author["rank"],
                "Composite Score": round(author["composite_score"], 2),
                "Citations": sum(author["citations"].values()),
                "Publications": sum(author["publications"].values()),
                "Self-citation Rate": round(sum(author["self_citations"].values()) / sum(author["citations"].values()) * 100, 2)
            }
            author_details = html.Div([
                html.H3(f"Details for {clicked_author}"),
                html.Ul([html.Li(f"{key}: {value}") for key, value in metrics.items()])
            ])

        return fig, author_details

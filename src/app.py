from dash import Dash
from data_loader import load_authors_data
from layout import create_layout
from callbacks import register_callbacks
from graph_builder import create_author_graph

# Load data
authors_data = load_authors_data("/content/authors.json")

# Create Dash app
app = Dash(__name__)

# Set app layout
app.layout = create_layout()

# Create the author graph
G = create_author_graph(authors_data)

# Register callbacks
register_callbacks(app, authors_data)

# Run server
if __name__ == "__main__":
    app.run_server(debug=True)

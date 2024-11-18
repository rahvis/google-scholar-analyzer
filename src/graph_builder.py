import networkx as nx
import plotly.graph_objects as go

def create_author_graph(authors_data):
    """
    Create a directed graph of authors based on their rankings and composite scores.

    Args:
    - authors_data (list): List of authors with ranks and scores.

    Returns:
    - NetworkX DiGraph: A directed graph representing author relationships.
    """
    G = nx.DiGraph()
    for author in authors_data:
        G.add_node(author["name"], rank=author["rank"], composite_score=author["composite_score"])
    return G

def generate_graph_figure(G, clicked_author=None):
    """
    Generate the Plotly figure for the author network graph.

    Args:
    - G (NetworkX DiGraph): The graph representing authors.
    - clicked_author (str): Name of the clicked author, if any.

    Returns:
    - go.Figure: Plotly figure for the graph visualization.
    """
    pos = nx.spring_layout(G)
    edge_x, edge_y, node_x, node_y, text, size = [], [], [], [], [], []

    # Create edge traces
    for edge in G.edges():
        x0, y0 = pos[edge[0]]
        x1, y1 = pos[edge[1]]
        edge_x.append(x0)
        edge_y.append(y0)
        edge_x.append(x1)
        edge_y.append(y1)
        edge_x.append(None)
        edge_y.append(None)
    edge_trace = go.Scatter(x=edge_x, y=edge_y, line=dict(width=0.5, color="#888"),
                            hoverinfo="none", mode="lines")

    # Create node traces
    for node in G.nodes():
        x, y = pos[node]
        node_x.append(x)
        node_y.append(y)
        size.append(20 if node == clicked_author else 10)
        text.append(node)
    node_trace = go.Scatter(
        x=node_x, y=node_y, mode="markers+text", hoverinfo="text",
        marker=dict(size=size, color="LightSkyBlue", line=dict(width=2)),
        text=text
    )

    fig = go.Figure(data=[edge_trace, node_trace],
                    layout=go.Layout(
                        title="Author Graph",
                        titlefont_size=16,
                        showlegend=False,
                        hovermode="closest",
                        margin=dict(b=0, l=0, r=0, t=40),
                        xaxis=dict(showgrid=False, zeroline=False),
                        yaxis=dict(showgrid=False, zeroline=False)
                    ))

    return fig

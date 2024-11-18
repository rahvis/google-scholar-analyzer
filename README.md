
# Author (Google Scholar) Rankings Dashboard

The simulation has been done on synthetic dataset. This visualizes the rankings of authors based on a composite score derived from their publication and citation data. The dashboard allows users to interactively explore a network of authors and view detailed metrics for each author.

## How It Works

1. **Data Loading:**
   - The data is loaded from a JSON file (`authors.json`), which contains information about authors, including their citations, publications, and collaborators.

2. **Composite Score Calculation:**
   - Each author's ranking is computed based on a composite score that considers:
     - Total citations
     - Self-citation rate
     - Collaboration dependency
   - The formula used to calculate the composite score is:
     ```python
     (citations * 0.4) - (self_citation_rate * 20) - (collaborator_dependency * 10)
     ```
   - The authors are sorted by this score, with higher scores indicating higher ranks.

3. **Network Visualization:**
   - A directed graph is created using `NetworkX`, where each author is represented as a node. The graph layout is generated using the `spring_layout` algorithm, which simulates a force-directed graph.
   - Authors are connected based on collaboration patterns, and the nodes are sized and colored based on their rank.

4. **Interactive Dash Application:**
   - The dashboard is built using `Dash` and `Plotly`. It features an interactive network graph where users can click on any author node to view more details about that author.
   - When a user clicks on a node, the following author metrics are displayed:
     - Rank
     - Composite Score
     - Citations
     - Publications
     - Self-citation Rate

## Requirements

- `dash`
- `plotly`
- `networkx`
- `json`

You can install the required dependencies using pip:

```bash
pip install dash plotly networkx

def calculate_composite_score(author):
    """
    Calculate the composite score for an author based on their citations, 
    self-citations, and collaboration dependency.

    Args:
    - author (dict): Author data containing citations, publications, and collaborators.

    Returns:
    - float: Composite score.
    """
    citations = sum(author["citations"].values())
    publications = sum(author["publications"].values())
    self_citation_rate = sum(author["self_citations"].values()) / (citations + 1)
    collaborator_dependency = author["collaborators"]["most_frequent"] / (publications + 1)
    return (citations * 0.4) - (self_citation_rate * 20) - (collaborator_dependency * 10)

def generate_rankings(authors_data):
    """
    Generate a sorted list of authors based on their composite scores.

    Args:
    - authors_data (list): List of author data.

    Returns:
    - List of authors with calculated ranks and composite scores.
    """
    authors_data = sorted(authors_data, key=calculate_composite_score, reverse=True)
    for rank, author in enumerate(authors_data, start=1):
        author["rank"] = rank
        author["composite_score"] = calculate_composite_score(author)
    return authors_data

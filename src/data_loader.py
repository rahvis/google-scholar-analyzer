import json

def load_authors_data(file_path):
    """
    Load authors' data from a JSON file.

    Args:
    - file_path (str): Path to the authors JSON file.

    Returns:
    - List of authors' data.
    """
    with open(file_path, 'r') as f:
        data = json.load(f)
    return data.get("authors", [])

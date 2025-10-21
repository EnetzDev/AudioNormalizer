import os

def resource_path(filename: str) -> str:
    """
    Returns the absolute path to a file in app/resources
    """
    # Directory of this utils.py file
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Go up one level to 'app'
    app_dir = os.path.abspath(os.path.join(current_dir, ".."))

    # Path to resources folder
    resources_dir = os.path.join(app_dir, "resources")

    return os.path.join(resources_dir, filename)
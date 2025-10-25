import toml
from pathlib import Path

def resource_path(filename: str) -> str:
    """
    Returns the absolute path to a file in app/resources
    """
    # Directory of this utils.py file
    current_dir = Path(__file__).resolve().parent

    # Go up one level to 'app' and into 'resources'
    resources_dir = current_dir.parent / "resources"

    return str(resources_dir / filename)
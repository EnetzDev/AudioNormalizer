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

def get_version() -> str:
    """
    Returns the version from pyproject.toml located two levels above this utils file.
    """

    # Directory of this utils.py file
    current_dir = Path(__file__).resolve().parent

    # Go up two levels to the project root
    project_root = current_dir.parent.parent

    # Path to pyproject.toml
    pyproject_path = project_root / "pyproject.toml"

    # Read and parse the TOML file
    try:
        pyproject = toml.load(pyproject_path)

        return pyproject["tool"]["poetry"]["version"]
    
    except FileNotFoundError:
        raise FileNotFoundError(f"pyproject.toml not found at {pyproject_path}")
    
    except KeyError:
        raise KeyError("Version key not found in pyproject.toml")
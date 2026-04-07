"""Tool to view/load images from the filesystem."""

from pathlib import Path
from langchain_core.tools import tool


@tool
def view_image(image_path: str) -> str:
    """Load and return an image file for display.

    Args:
        image_path: Path to the image file

    Returns:
        A marker string containing the image path for middleware to process
    """
    path = Path(image_path)
    if not path.exists():
        return f"Error: image file not found at {path}"

    if not path.is_file():
        return f"Error: path is not a file: {path}"

    return f"image_path:{path.absolute()}"

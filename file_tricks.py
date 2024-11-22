from pathlib import Path

def read_file(file_path):
    """Read a file and return its contents."""
    path = Path(file_path)
    if path.is_file():
        with path.open('r') as file:
            return file.read()
    return None

def write_file(file_path, content):
    """Write content to a file."""
    path = Path(file_path)
    with path.open('w') as file:
        file.write(content)

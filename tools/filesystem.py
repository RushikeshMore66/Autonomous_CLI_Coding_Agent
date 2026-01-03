from pathlib import Path

def read_file(file_path: str) -> str:
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"File {path} does not exist")
    if not path.is_file():
        raise ValueError(f"{path} is not a file")
    return path.read_text(encoding="utf-8")

def write_file(file_path: str, content: str) -> None:
    Path(file_path).write_text(content, encoding="utf-8")

from pathlib import Path


def read_logs(file_path: str):

    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(
            f"Log file not found: {file_path}"
        )

    with open(path, "r", encoding="utf-8") as file:
        return [
            line.strip()
            for line in file
            if line.strip()
        ]
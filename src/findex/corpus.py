from pathlib import Path
from typing import Iterator

def iter_documents(data_dir: Path | str) -> Iterator[str]:
    for file_path in Path(data_dir).rglob("*.txt"):
        if file_path.is_file():
            with file_path.open(encoding="utf-8") as f:
                yield f.read()
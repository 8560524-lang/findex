import re
import unicodedata
from typing import Iterator

TOKEN_RE = re.compile(r"[\w\'-]+")


def tokenize(text: str) -> Iterator[str]:
    normalized = unicodedata.normalize("NFC", text)
    folded = normalized.casefold()

    for match in TOKEN_RE.finditer(folded):
        yield match.group(0)
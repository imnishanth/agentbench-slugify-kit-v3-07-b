import re
import unicodedata
__version__ = "2.0.0"

def slugify(text: str, sep: str = "-", max_len: int | None = None) -> str:
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    text = re.sub(r"[^A-Za-z0-9]+", sep, text).strip(sep).lower()
    if max_len:
        text = text[:max_len].rstrip(sep)
    return text

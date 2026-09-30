"""Site configuration, and the one place that knows how to build a WhatsApp link.

The page builder and the page modules both need these, so they live here rather
than in either of them.
"""
import json
import pathlib
import re
import urllib.parse

ROOT = pathlib.Path(__file__).resolve().parent.parent
SITE = json.loads((ROOT / "tools" / "site.json").read_text())


def wa_number():
    """wa.me takes the number as digits only: no plus, spaces or dashes."""
    return re.sub(r"\D", "", SITE.get("whatsapp") or "")


def wa_href(message=""):
    """A link that opens WhatsApp, empty when no number is configured."""
    num = wa_number()
    if not num:
        return ""
    if not message:
        return f"https://wa.me/{num}"
    return f"https://wa.me/{num}?text={urllib.parse.quote(message)}"

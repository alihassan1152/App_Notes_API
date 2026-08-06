# ============================================
# Utils — chhote reusable helper functions
# extract_links: content se [[wiki-links]] nikalta hai
# ============================================
import re

def extract_links(content: str) -> list[str]:
    """content mein se saare [[wiki links]] ke naam nikal lo"""
    pattern = r"\[\[(.*?)\]\]"
    return re.findall(pattern, content)

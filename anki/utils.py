from random import randint
import re


def gen_id() -> int:
    """Generate a deck id."""
    return randint(1000000000, 9999999999)


def gen_html_list(items: list[str], list_type) -> str:
    """
    Generate an ordered list from html.

    Args:
        items: The items in the list.
        list_type: The type of list. Either "ol" or "ul".
    """
    output = f"<{list_type}>"
    for item in items:
        output += f"<li>{item}</li>"
    output += f"</{list_type}>"
    return output


def gen_formatted_html(text: str) -> str:
    output = text

    for match in re.findall(r"\*.*\*", text):
        output.replace(match, f"<i>{text}</i>")
    for match in re.findall(r"\b.*\b", text):
        output.replace(match, f"<b>{text}</b>")
    for match in re.findall(r"__.*__", text):
        output.replace(match, f"<u>{text}</u>")

    return output

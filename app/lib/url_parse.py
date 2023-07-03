from typing import List

import requests
from bs4 import BeautifulSoup


class ElementInfo:
    def __init__(self, importance: int, tag: str, text: str):
        self.importance = importance
        self.tag = tag
        self.text = text

    def __repr__(self):
        return f"Importance: {self.importance}; HTML_Tag: {self.tag}; Text: {self.text}"


def extract_text(element):
    if element.string:
        return element.string.strip().replace("\n", " ")
    else:
        return ""


def rate_text(element):
    tag_weights = {
        "h1": 3,
        "h2": 2,
        "h3": 1,
        "p": 1,
        "strong": 2,
        "em": 2,
        "blockquote": 2,
        "div": 0.5,
        "span": 0.5,
        "a": 0.5,
        "button": 1,
        "li": 0.8,
    }
    tag = element.name
    return tag_weights.get(tag, 0)


def process_element(element, depth, element_list):
    if element.name == "script":  # Skip script tags
        return

    if element.name == "style":  # Skip script tags
        return

    text = extract_text(element)
    tag_weight = rate_text(element)
    importance = round(100 * ((tag_weight + len(text) / 10) / (depth + 1)))
    if text and len(text) > 10:
        element_info = ElementInfo(importance=importance, tag=element.name, text=text)
        element_list.append(element_info)
    for child in element.children:
        if child.name:
            process_element(child, depth + 1, element_list)


def cut_list_under_limit(strings: List[ElementInfo], limit: int):
    total_characters = 0
    result = []

    for string in strings:
        total_characters += len(string.text)

        if total_characters <= limit:
            result.append(string)
        else:
            break

    return result


def get_rated_elements(url: str, char_limit: int = 0):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    root_element = soup.find("body")
    elements = []
    process_element(root_element, 0, elements)

    deduplicated_elements = list(
        {element.text: element for element in elements}.values()
    )
    sorted_elements = sorted(deduplicated_elements, key=lambda x: -x.importance)

    if char_limit > 0:
        sorted_elements = cut_list_under_limit(sorted_elements, char_limit)

    return sorted_elements


if __name__ == "__main__":
    input_url = "https://countly.cz/"
    for element in get_rated_elements(input_url):
        print(element)

import logging
from typing import List

import requests
from bs4 import BeautifulSoup

from app.lib.text import filter_out_similar
from app.lib.element import ElementInfo


log = logging.getLogger("app")


def extract_text(element):
    if element.string:
        return element.string.strip().replace("\n", " ")
    else:
        return ""


def rate_text(element):
    tag_weights = {
        "h1": 10,
        "h2": 6,
        "h3": 3,
        "p": 2,
        "strong": 4,
        "em": 3,
        "blockquote": 2,
        "div": 1,
        "span": 1,
        "a": 3,
        "button": 20,
        "li": 3,
        "meta": 999,
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
    importance = round(100 * ((tag_weight + min(len(text) / 10, 50)) / (depth + 1)))
    if text and len(text) > 5:
        element_info = ElementInfo(importance=importance, tag=element.name, text=text)
        element_list.append(element_info)
    for child in element.children:
        if child.name:
            process_element(child, depth + 1, element_list)


def process_metatags(meta_tags, elements):
    for tag in meta_tags:
        if tag.get("name") in ("description",):
            text = tag.get("content")
            if text:
                element_info = ElementInfo(importance=999, tag="meta", text=text)
                elements.append(element_info)


def process_html_tree(element, indent=0, indent_max=100, tree=[], balancer={0: 1}):
    if indent <= indent_max:
        if indent in balancer.keys():
            balancer[indent] += 1
        else:
            balancer[indent] = 1

        if balancer[indent] < 3:
            # print('-' * indent + element.name)
            tree.append("-" * indent + element.name)

    for child in element.children:
        if child.name is not None:
            if indent in balancer.keys():
                balancer[indent] += 1
            else:
                balancer[indent] = 1
            process_html_tree(child, indent + 1, indent_max, tree, balancer)


def process_html_stats(root_element):
    # Find all image tags
    images = root_element.find_all("img")
    num_images = len(images)

    # Find all text content
    text_elements = root_element.find_all(text=True)
    text = " ".join(text_elements).strip()
    text_length = len(text)

    return ElementInfo(
        importance=777,
        tag="html_info",
        text=f"There are {num_images} images and total length of text is {text_length} letters.",
    )


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


def get_rated_elements(url: str, char_limit: int = 0) -> List[ElementInfo]:
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    root_element = soup.find("body")
    elements = []
    process_metatags(meta_tags=soup.find_all("meta"), elements=elements)

    tree = []
    process_html_tree(root_element, tree=tree)
    elements.append(
        ElementInfo(importance=888, tag="html_tree", text="\n".join(tree)[:300])
    )
    elements.append(process_html_stats(root_element))

    process_element(root_element, 0, elements)

    deduplicated_elements = list(
        {element.text: element for element in elements}.values()
    )
    deduplicated_elements = filter_out_similar(
        elements_list=deduplicated_elements,
    )
    sorted_elements = sorted(deduplicated_elements, key=lambda x: -x.importance)

    if char_limit > 0:
        sorted_elements = cut_list_under_limit(sorted_elements, char_limit)

    return sorted_elements


if __name__ == "__main__":
    input_url = "https://countly.cz/"
    for element in get_rated_elements(input_url):
        print(element)

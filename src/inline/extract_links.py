import re


def extract_markdown_images(text) -> list[tuple[str, str]]:
    extracted_links = []
    image_pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    for match in re.finditer(image_pattern, text):
        alt_text = match.group(1)
        image_url = match.group(2)
        extracted_links.append((alt_text, image_url))
    return extracted_links


def extract_markdown_links(text) -> list[tuple[str, str]]:
    extracted_links = []
    link_pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    for match in re.finditer(link_pattern, text):
        link_text = match.group(1)
        link_url = match.group(2)
        extracted_links.append((link_text, link_url))
    return extracted_links

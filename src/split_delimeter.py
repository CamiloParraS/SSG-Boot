import re

from nodes import TextNode, TextType


def split_nodes_delimiter(
    old_nodes: list[TextNode], delimiter: str, text_type: TextType
) -> list[TextNode]:

    HTMLnodes = []

    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            HTMLnodes.append(old_node)
            continue
        split_node = []
        section = old_node.text.split(delimiter)
        if len(section) % 2 == 0:
            raise ValueError("Delimiter count is not even")
        for i in range(len(section)):
            if section[i] == "":
                continue
            if i % 2 == 0:
                split_node.append(TextNode(section[i], TextType.TEXT))
            else:
                split_node.append(TextNode(section[i], text_type))
        HTMLnodes.extend(split_node)
    return HTMLnodes


def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    split_nodes = []
    pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"

    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            split_nodes.append(old_node)
            continue
        text = old_node.text
        matches = re.findall(pattern, text)

        if not matches:
            split_nodes.append(old_node)
            continue
        current_text = text
        for alt_text, url in matches:
            sections = current_text.split(f"![{alt_text}]({url})", 1)

            if len(sections) != 2:
                continue

            if sections[0]:
                split_nodes.append(TextNode(sections[0], TextType.TEXT))

            split_nodes.append(TextNode(alt_text, TextType.IMAGE, url=url))

            current_text = sections[1]

        if current_text != "":
            split_nodes.append(TextNode(current_text, TextType.TEXT))

    return split_nodes


def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    split_nodes = []
    pattern = r"(?<!\!)\[([^\[\]]*)\]\(([^\(\)]*)\)"

    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            split_nodes.append(old_node)
            continue
        text = old_node.text
        matches = re.findall(pattern, text)

        if not matches:
            split_nodes.append(old_node)
            continue
        current_text = text
        for alt_text, url in matches:
            sections = current_text.split(f"[{alt_text}]({url})", 1)

            if len(sections) != 2:
                continue

            if sections[0]:
                split_nodes.append(TextNode(sections[0], TextType.TEXT))

            split_nodes.append(TextNode(alt_text, TextType.LINKS, url=url))

            current_text = sections[1]

        if current_text != "":
            split_nodes.append(TextNode(current_text, TextType.TEXT))

    return split_nodes


def text_to_textnodes(text: str) -> list[TextNode]:
    nodes = [TextNode(text, TextType.TEXT)]
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE_TEXT)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes

from enum import Enum


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    OREDERED_LIST = "ordered_list"


def markdown_to_blocks(md: str) -> list[str]:
    blocks = []
    current_block = ""

    for line in md.split("\n"):
        if line == "":
            if current_block != "":
                blocks.append(current_block.strip())
                current_block = ""
        else:
            if current_block == "":
                current_block = line
            else:
                current_block += "\n" + line

    if current_block != "":
        blocks.append(current_block.strip())

    return blocks

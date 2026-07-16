from nodes import TextNode, TextType

def main():
    example_one = TextNode("Hello, World!", TextType.LINKS, "https://en.wikipedia.org/wiki/Hello,_world")
    print(example_one)

if __name__ == "__main__":
    main()

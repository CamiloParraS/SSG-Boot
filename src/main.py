import os
import shutil
import sys

from blocks.markdown_blocks import markdown_to_html_node


def main():
    base_path = sys.argv[1] if len(sys.argv) > 0 else "/"
    copy_from_static_to_public_or_whatever()
    generate_pages_recursive("content", "template.html", "docs", base_path)


def copy_from_static_to_public_or_whatever(from_path="static", to_path="public"):
    if not os.path.exists(to_path):
        os.makedirs(to_path)
    for file in os.listdir(to_path):
        file_path = os.path.join(to_path, file)
        if os.path.isfile(file_path) or os.path.islink(file_path):
            os.remove(file_path)
            print(f"Removed file: {file_path}")
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)
            print(f"Removed directory: {file_path}")

    for file in os.listdir(from_path):
        src_path = os.path.join(from_path, file)
        dst_path = os.path.join(to_path, file)
        if os.path.isfile(src_path):
            shutil.copy2(src_path, dst_path)
            print(f"Copied file: {src_path} to {dst_path}")
        elif os.path.isdir(src_path):
            shutil.copytree(src_path, dst_path)
            print(f"Copied directory: {src_path} to {dst_path}")


def extract_tittle(md: str) -> str:
    lines = md.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:].strip()
    raise Exception("No title found in the markdown content.")


def generate_html_from_markdown(from_path, template_path, dest_path, base_path) -> str:
    print(
        f"Generating page from {from_path} using template {template_path} and saving to {dest_path}"
    )
    with open(from_path, "r", encoding="utf-8") as f:
        md_content = f.read()
    with open(template_path, "r", encoding="utf-8") as f:
        template_content = f.read()

    markdown_html = markdown_to_html_node(md_content)
    html = markdown_html.to_html()
    title = extract_tittle(md_content)

    final_html = template_content.replace("{{ Content }}", html).replace(
        "{{ Title }}", title
    )

    final_html = final_html.replace('href="/', f'href="{base_path}')
    final_html = final_html.replace('src="/', f'src="{base_path}')

    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(final_html)


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, base_path):
    for root, dirs, files in os.walk(dir_path_content):
        for file in files:
            if file.endswith(".md"):
                from_path = os.path.join(root, file)
                relative_path = os.path.relpath(from_path, dir_path_content)
                dest_path = os.path.join(dest_dir_path, relative_path)
                dest_path = os.path.splitext(dest_path)[0] + ".html"
                dest_dir = os.path.dirname(dest_path)
                if not os.path.exists(dest_dir):
                    os.makedirs(dest_dir)

                generate_html_from_markdown(
                    from_path, template_path, dest_path, base_path
                )


if __name__ == "__main__":
    main()

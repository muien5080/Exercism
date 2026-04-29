import re


def parse(markdown: str) -> str:
    lines = markdown.split('\n')
    result = []
    in_list = False

    for line in lines:
        # Handle headers
        header = parse_header(line)
        if header:
            if in_list:
                result.append('</ul>')
                in_list = False
            result.append(header)
            continue

        # Handle list items
        list_item = parse_list_item(line)
        if list_item:
            if not in_list:
                result.append('<ul>')
                in_list = True
            result.append(list_item)
            continue
        else:
            if in_list:
                result.append('</ul>')
                in_list = False

        # Handle paragraph
        paragraph = f"<p>{apply_inline_formatting(line)}</p>"
        result.append(paragraph)

    if in_list:
        result.append('</ul>')

    return ''.join(result)


def parse_header(line: str) -> str | None:
    """
    Detects Markdown headers (# to ######) and converts to HTML.
    """
    for i in range(6, 0, -1):
        prefix = '#' * i + ' '
        if line.startswith(prefix):
            content = line[len(prefix):]
            return f"<h{i}>{content}</h{i}>"
    return None


def parse_list_item(line: str) -> str | None:
    """
    Detects list items starting with '* '.
    """
    match = re.match(r'\* (.*)', line)
    if not match:
        return None

    content = apply_inline_formatting(match.group(1))
    return f"<li>{content}</li>"


def apply_inline_formatting(text: str) -> str:
    """
    Applies bold (__text__) and italic (_text_) formatting.
    """

    # Bold: __text__
    text = re.sub(r'__(.*?)__', r'<strong>\1</strong>', text)

    # Italic: _text_
    text = re.sub(r'_(.*?)_', r'<em>\1</em>', text)

    return text
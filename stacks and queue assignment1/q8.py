def match_tags(html_code):
    stack = []
    open_tags = {}
    for char in html_code:
        if char == "<":
            tag_name, attrs = get_tag_name_and_attributes(char)
            if tag_name in open_tags:
                print("Tag {} is already open".format(tag_name))
            open_tags[tag_name] = attrs
            stack.append(tag_name)
        elif char == ">":
            if len(stack) == 0:
                print("Unmatched closing tag")
            top_tag = stack.pop()
            if top_tag != open_tags.pop(top_tag):
                print("Mismatched tags")
    return len(stack) == 0


def get_tag_name_and_attributes(char):
    tag_name = ""
    attrs = {}
    while char != ">":
        if char == " ":
            continue
        if char == "/":
            break
        tag_name += char
        char = html_code[1]
    if char == "/":
        return tag_name, {}
    for i in range(2, len(html_code)):
        if html_code[i] == ">":
            break
        key, value = html_code[i:i + 2]
        attrs[key] = value
    return tag_name, attrs


if __name__ == "__main__":
    html_code = "<html><head><title>This is a title</title></head><body><h1>This is a heading</h1></body></html>"
    print(match_tags(html_code))

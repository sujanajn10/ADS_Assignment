def match_tags(html_code):
    stack = []
    for char in html_code:
        if char == "<":
            stack.append(char)
        elif char == ">":
            if len(stack) == 0:
                print("Unmatched closing tag")
            top_tag = stack.pop()
            if top_tag != "<":
                print("Mismatched tags")
    return len(stack) == 0


if __name__ == "__main__":
    html_code = "<html><head><title>This is a title</title></head><body><h1This is a heading</h1></body></html>"
    print(match_tags(html_code))

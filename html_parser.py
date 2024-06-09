import sys

def alpha(char):
    return ('a' <= char <= 'z') or ('A' <= char <= 'Z') or ('0' <= char <= '9')

def start_state(char):
    if char == "<":
        return "CHECK", ""
    return "END", ""

def check_state(char, curr_tag):
    if char == "/":
        curr_tag += char
        return "TAG_CLOSE", curr_tag
    elif alpha(char):
        curr_tag += char
        return "TAG_NAME", curr_tag
    return "END", curr_tag

def tag_name_state(char, curr_tag):
    if alpha(char):
        curr_tag += char
        return "TAG_NAME", curr_tag
    elif char == ">":
        return "END", curr_tag
    return "END", curr_tag

def tag_close_state(char, curr_tag):
    if alpha(char):
        curr_tag += char
        return "TAG_CLOSE", curr_tag
    elif char == ">":
        return "END", curr_tag
    return "END", curr_tag

def recog(token):
    curr_state = "START"
    curr_tag = ""
    acc_tags = ['html', 'head', 'body', 'title', 'h1', 'p', 'nav']

    for char in token:
        if curr_state == "START":
            curr_state, curr_tag = start_state(char)
        elif curr_state == "CHECK":
            curr_state, curr_tag = check_state(char, curr_tag)
        elif curr_state == "TAG_NAME":
            curr_state, curr_tag = tag_name_state(char, curr_tag)
        elif curr_state == "TAG_CLOSE":
            curr_state, curr_tag = tag_close_state(char, curr_tag)
        elif curr_state == "END":
            break

    if curr_state == "END" and (curr_tag in acc_tags or (len(curr_tag) > 1 and curr_tag[0] == "/" and curr_tag[1:] in acc_tags)):
        return curr_tag

    return None

def closetag(html, start):
    pos = start
    while pos < len(html):
        if html[pos] == ">":
            return pos
        pos += 1
    return -1

def parse_html(html):
    stack = ["#"]
    pos = 0
    head_found = False
    body_found = False
    html_found = False
    title_found = False

    while pos < len(html):
        if html[pos] == "<":
            end_pos = closetag(html, pos)
            if end_pos == -1:
                return "Rejected"
            tag = html[pos:end_pos + 1]
            tag_name = recog(tag)
            if tag_name is None:
                return "Rejected"
            if tag_name == "html":
                html_found = True
            if tag_name == "head":
                if body_found:
                    return "Rejected"  # <head> tidak boleh muncul setelah <body>
                head_found = True
            if tag_name == "body":
                if not html_found:
                    return "Rejected" #body harus ada di dalam html
                elif stack[-1] == "head":
                    if head_found:
                        return "Rejected" # <body> harus ada di dalam <html> dan gaboleh diantara tag head
                body_found = True
            if tag_name == "title":
                if not head_found or head_found and body_found:
                    return "Rejected"  # <title> harus ada di dalam <head> dan sebelum <body>
                title_found = True
            if not (len(tag_name) > 1 and tag_name[0] == "/"):
                stack.append(tag_name)
            else:
                if len(stack) == 0 or stack[-1] != tag_name[1:]:
                    return "Rejected"
                if stack[-1] == "head":
                    if not title_found:
                        return "Rejected"
                stack.pop()

            pos = end_pos
        pos += 1

    if html_found and len(stack) == 1 and stack[-1] == "#":
        stack.pop()  # Pop the # symbol
        # Accept if all necessary tags are found and properly nested
        if head_found and body_found and title_found:
            return "Accepted"
        if not head_found and not body_found and not title_found:
            return "Accepted"
        # Accept if all necessary tags are found and properly nested
        if head_found or body_found:
            return "Accepted"
    
    return "Rejected"

def main():
    if len(sys.argv) != 2:
        print("Usage: python html_parser.py <filename>")
        return

    filename = sys.argv[1]

    try:
        with open(filename, 'r') as file:
            html_content = file.read()
    except FileNotFoundError:
        print(f"File not found: {filename}")
        return

    # Print the content of the HTML file
    print("Isi file HTML:")
    print(html_content)
    print()

    result = parse_html(html_content)
    print(f"Hasil: {result}")

if __name__ == "__main__":
    main()

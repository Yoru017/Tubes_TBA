def alpha(char):
    return ('a' <= char <= 'z') or ('A' <= char <= 'Z') or ('0' <= char <= '9')

def start_state(char):
    if char == "<":
        return "CHECK", ""
    return "INVALID", ""

def check_state(char, curr_tag):
    if char == "/":
        curr_tag += char
        return "TAG_CLOSE", curr_tag
    elif alpha(char):
        curr_tag += char
        return "TAG_NAME", curr_tag
    return "INVALID", curr_tag

def tag_name_state(char, curr_tag):
    if alpha(char):
        curr_tag += char
        return "TAG_NAME", curr_tag
    elif char == ">":
        return "END", curr_tag
    return "INVALID", curr_tag

def tag_close_state(char, curr_tag):
    if alpha(char):
        curr_tag += char
        return "TAG_CLOSE", curr_tag
    elif char == ">":
        return "END", curr_tag
    return "INVALID", curr_tag

def end_state(char, curr_tag):
    return "INVALID", curr_tag

def recog(token):
    curr_state = "START"
    curr_tag = ""
    acc_tags = ['html', 'head', 'body', 'title', 'h2', 'p', 'img']

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
            curr_state, curr_tag = end_state(char, curr_tag)
        elif curr_state == "INVALID":
            break

    if curr_state == "END" and (curr_tag in acc_tags or (len(curr_tag) > 1 and curr_tag[0] == "/" and curr_tag[1:] in acc_tags)):
        return "ACCEPTED"

    return "REJECTED"

def main():
    print("Masukkan token HTML (ketik 'exit' untuk keluar):")
    while True:
        token = input("Token: ")
        tag = token.lower()
        if token.lower() == 'exit':
            break
        result = recog(tag)
        print(f"Token: {token}, Result: {result}")

if __name__ == "__main__":
    main()

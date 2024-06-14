<<<<<<< HEAD
import sys, recog

# Tokenizer function
def tokenize(teks):
    tokens = []
    pos = 0
    while pos < len(teks):
        token = cek_dfa(teks[pos:])
        if token:
            tokens.append(token)
            pos = pos + len(token)
        else:
            pos += 1
    return tokens

def cek_dfa(text):
    for length in range(1, len(text) + 1):
        if recog.recog(text[:length]) == "ACCEPTED":
            return text[:length]
    return None

def parser(input,parse_table):
    stack = []
    stack.append('#')
    stack.append('S')
    input.append('EOS')
    i = 0
    while stack[-1]!='#': #looping hingga isi stack teratas adalah #
        read = input[i] #LL(1)
        top = stack.pop()
        if top in parse_table: #jika top daripada stack berupa non terminal
            if read in parse_table[top]: #kalau 'read/symbol' ada di parse table 
                produksi = parse_table[top][read] # 
                if produksi !='':
                    stack.extend(reversed(produksi.split())) #push hasil produksi ke stack secara terbalik
            else:
                return False
        else: #jika top daripada stack berupa terminal
            if top == read:
                i= i+1 #input maju
            else:
                return False
    top = stack.pop()
    return stack == [] and top == "#"

#mendefinisikan grammar dan parser table
grammar = {
    'S': ['<html> A </html>'],
    'A': ['<head> D </head> B','B',''],
    'B': ['<body> C </body>', ''],
    'C': ['<h1> </h1> C', '<p> </p> C', ''],
    'D': ['<title> </title>', ''],
}
parse_table = {
    'S': {
        '<html>': '<html> A </html>',
    },
    'A': {
        '<head>': '<head> D </head> B',
        '<body>': 'B',
        '</html>': '',
    },
    'B': {
        '<body>': '<body> C </body>',
        '</html>': ''
    },
    'C': {
        '<h1>': '<h1> </h1> C', 
        '<p>': '<p> </p> C',
        '</body>': '',
    },
    'D': {
       '<title>': '<title> </title>',
       '</head>': ''
    }
}

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

    # Menampilkan isi tag yang ada pada file HTML
    print("Isi file tag pada file HTML:")
    token_html = tokenize(html_content)
    print(token_html)

    print(parser(token_html,parse_table))

if __name__ == "__main__":
=======
import sys, recog

# Tokenizer function
def tokenize(teks):
    tokens = []
    pos = 0
    while pos < len(teks):
        token = cek_dfa(teks[pos:])
        if token:
            tokens.append(token)
            pos = pos + len(token)
        else:
            pos += 1
    return tokens

def cek_dfa(text):
    for length in range(1, len(text) + 1):
        if recog.recog(text[:length]) == "ACCEPTED":
            return text[:length]
    return None

def parser(input,parse_table):
    stack = []
    stack.append('#')
    stack.append('S')
    input.append('EOS')
    i = 0
    while stack[-1]!='#': #looping hingga isi stack teratas adalah #
        read = input[i] #LL(1)
        top = stack.pop()
        if top in parse_table: #jika top daripada stack berupa non terminal
            if read in parse_table[top]: #kalau 'read/symbol' ada di parse table 
                produksi = parse_table[top][read] # 
                if produksi !='':
                    stack.extend(reversed(produksi.split())) #push hasil produksi ke stack secara terbalik
            else:
                return False
        else: #jika top daripada stack berupa terminal
            if top == read:
                i= i+1 #input maju
            else:
                return False
    top = stack.pop()
    return stack == [] and top == "#"

#mendefinisikan grammar dan parser table
grammar = {
    'S': ['<html> A </html>'],
    'A': ['<head> D </head> B','B',''],
    'B': ['<body> C </body>', ''],
    'C': ['<h1> </h1> C', '<p> </p> C', ''],
    'D': ['<title> </title>', ''],
}
parse_table = {
    'S': {
        '<html>': '<html> A </html>',
    },
    'A': {
        '<head>': '<head> D </head> B',
        '<body>': 'B',
        '</html>': '',
    },
    'B': {
        '<body>': '<body> C </body>',
        '</html>': ''
    },
    'C': {
        '<h1>': '<h1> </h1> C', 
        '<p>': '<p> </p> C',
        '</body>': '',
    },
    'D': {
       '<title>': '<title> </title>',
       '</head>': ''
    }
}

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

    # Menampilkan isi tag yang ada pada file HTML
    print("Isi file tag pada file HTML:")
    token_html = tokenize(html_content)
    print(token_html)

    print(parser(token_html,parse_table))

if __name__ == "__main__":
>>>>>>> 4f40eed7d36322284a155739551c5150af36d496
    main()
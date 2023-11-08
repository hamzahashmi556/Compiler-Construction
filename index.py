import re

# Define token types
TOKEN_TYPES = [
    ('NEWLINE', r'\n'),
    ('KEYWORD', r'(interface|Main|func|let|var|static|for|while|if|else '
                r'if|elif|else|concat|pow|sqrt|class|init|deinit|public|protected|private|super|abstract|this|is_int'
                r'|is_char|is_float|is_bool|is_str|replace|find|len|interface)'),
    ('DATATYPE', r'(int|float|char|str|bool)'),
    ('CHAR', r'"[^"]{1}"|\'[^\']{1}\''),
    ('STRING', r'"[^"]"|\'[^\']\''),
    ('IDENTIFIER', r'[a-zA-Z_][a-zA-Z0-9_]*'),
    ('FLOAT', r'\b[0-9]+\.[0-9]+\b'),
    ('INT', r'\b[0-9]+\b'),
    ('NULL', r'null'),
    ('BOOLEAN', r'(true|false)'),
    # ('COMMENT', r'(//.|/\(.|\n)\/)'),
    ('OPERATOR',
     r',|=>|;|\(|\)|\{|\}|\:|\:\:|\.|\+=|-=|\=|\+\+|--|&&|\|\||===|==|!==|!=|<=|>=|\\|\+|-|\|/|>|<|=')
]


def tokenize(source_code):
    tokens = []
    line_no = 1
    while source_code:

        for token_type, pattern in TOKEN_TYPES:

            match = re.match(pattern, source_code, re.IGNORECASE)
            if match:
                # print("\n")
                # print("----------PATTERN--------")
                # print(f"{pattern}")
                # print("--------SOURCECODE--------")
                # print(source_code)
                # print("\n")
                value = match.group(0)
                if token_type == 'NEWLINE':
                    line_no += 1
                elif token_type == 'OPERATOR':
                    tokens.append((value, value, line_no))
                else:
                    tokens.append((token_type, value, line_no))
                source_code = source_code[len(value):]
                break
        else:
            print(f"Unexpected character: {source_code[0]}")
            source_code = source_code[len(value):]
            # break
            # raise SyntaxError(f"Unexpected character: {source_code[0]}")

    return tokens


if __name__ == '__main__':
    with open("mySourceCode", "r") as file:
        source_code = file.read()

    tokens = tokenize(source_code)
    for token_type, value, line_no in tokens:
        print([token_type, value, line_no])

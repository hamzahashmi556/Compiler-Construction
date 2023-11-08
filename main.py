# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


import re

# Define token types
TOKEN_TYPES = [
    ('KEYWORD', r'(Main|let|var|class|init|func|print|self)'),  # KEYWORDS
    ('IDENTIFIER', r'[a-zA-Z_][a-zA-Z0-9_]*'),                  # IDENTIFIERS E.G VARIBLES, METHODS, CLASS NAMES ETC
    ('CONSTANT', r'[0-9]+(\.[0-9]*)?'),                         # DIGITS
    ('DYNAMIC', r'[0-9]+'),
    ('STRING', r'"[^"]*"'),                                     # "" STRING
    ('COMMENT', r'//.*'),                                       # // COMMENT
    ('OPEN_BRACE', r'{'),                                       # BODY START {
    ('CLOSE_BRACE', r'}'),                                      # BODY END.}
    ('OPEN_PAREN', R'\('),                                      # PARAMETER START (
    ('CLOSE_PAREN', R'\)'),                                     # PARAMETER END (
    ('COLON', r':'),                                            # STATEMENT END :
    ('EQUALS', r'='),                                           # OPERATOR = ASSIGNS VALUE
    ('DOT', r'\.'),                                             # FLOATING POINT OR METHOD ACCESS .
    ('ADD', r'\+'),                                             # OPERATOR = ADDITION +
    ('MINUS', r'\-'),                                           # OPERATOR = SUBTRACTION -
    ('ASTERISK', r'\*'),                                        # OPERATOR = MULTIPLICATION *
    ('SLASH', r'\/'),                                           # OPERATOR = DIVISION /
]


def tokenize(source_code):
    tokens = []
    while source_code:

        for token_type, pattern in TOKEN_TYPES:
            # print("Token Type: ", token_type)
            # print("Pattern: ",pattern)
            # print("Source Code: ", source_code)
            match = re.match(pattern, source_code)
            if match:
                value = match.group(0)
                tokens.append((token_type, value))
                source_code = source_code[len(value):].lstrip()
                break
        else:
            print(f"Unexpected character: {source_code[0]}")
            # raise SyntaxError(f"Unexpected character: {source_code[0]}")

    return tokens


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Read source code from a file
    with open("mySourceCode", "r") as file:
        source_code = file.read()

    tokens = tokenize(source_code)
    for token_type, value in tokens:
        print(f"Token Type: {token_type}, Value: {value}")

import re

# Define token types
TOKEN_TYPES = [
    ('NEW_LINE', r'\n'),
    ('NULL_DATATYPE', r'\b(null)\b'),
    ('BOOLEAN_DATATYPE', r'\b(true|false)\b'),
    ('CHAR_DATATYPE', r'"[^"]{1}"|\'[^\']{1}\''),
    ('STRING_DATATYPE', r'"[^"]*"|\'[^\']*\''),
    ('FLOAT_DATATYPE', r'[0-9]*\.[0-9]+'),
    ('INT_DATATYPE', r'[0-9]+'),
    ('MAIN_KEYWORDS', r'\b(Main)\b'),
    ('FUNCTION_KEYWORDS', r'\b(func)\b'),
    ('VARIABLE_KEYWORDS', r'\b(let|var)\b'),
    ('STATIC_KEYWORD', r'\b(static)\b'),
    ('LOOP_KEYWORDS', r'\b(for|while)\b'),
    ('CONDITIONAL_KEYWORDS', r'\b(if|else\s*if|elif|else)\b'),
    ('ARRAY_STRING_OPERATIONS', r'\b(concat|replace|find|len)\b'),
    ('MATH_KEYWORDS', r'\b(pow|sqrt|range)\b'),
    ('CLASS_DECLARATION_KEYWORDS', r'\b(class)\b'),
    ('INITIALIZER_KEYWORDS', r'\b(init|deinit)\b'),
    ('INHERITANCE_KEYWORDS', r'\b(super|abstract|this|override)\b'),
    ('ACCESS_MODIFIERS_KEYWORDS', r'\b(private|protected|public)\b'),
    ('UTILITY_KEYWORDS', r'\b(return|print|exit)\b'),
    ('DATATYPE_KEYWORDS', r'\b(int|float|char|str|bool)\b'),
    ('IDENTIFIER', r'[a-zA-Z_][a-zA-Z0-9_]*'),
    ('COMMENT', r'(//.*|/\*(.|\n)*\*/)'),
    ('COMPARISON_OP', r'===|==|!==|!=|<=|>=|>|<'),
    ('INC_DEC_OP', r'\+\+|--'),
    ('ASSIGNMENT_OP', r'\+=|-=|\*=|\%=|='),
    ('POWER_OP', r'\*\*'),
    ('MULTIPLICATIVE_OP', r'\*|/|%'),
    ('ADDITIVE_OP', r'\+|-'),
    ('LOGICAL_OP', r'&&|\|\|'),
    ('COLON_OP', r':'),
    ('END_STATEMENT_OP', r';'),
    ('COMMA_OP', r','),
    ('DOT_OP', r'\.'),
    ('PARENTHESIS_OP', r'\(|\)'),
    ('BRACES_OP', r'\{|\}'),
    ('BRACKETS_OP', r'\[|\]'),
    ('NOT_OP', r'!'),
    ('DICTIONARY_OP', r'=>'),
    ('SPACE', r' ')
]

def tokenize(source_code):
    tokens = []
    line_no = 1
    while source_code:
        for token_type, pattern in TOKEN_TYPES:
            match = re.match(pattern, source_code, re.IGNORECASE)
            if match:
                value = match.group(0)
                if value != ' ':
                    if token_type == 'NEW_LINE':
                        line_no += 1
                    # elif token_type == 'OPERATOR':
                    #     tokens.append((value, value, line_no))
                    else:
                        tokens.append((token_type, value, line_no))
                        if token_type == 'COMMENT':
                            str_lines = value.count('\n')
                            if str_lines > 0:
                                line_no += str_lines
                        elif token_type in ['STRING_DATATYPE']:
                            comment_lines = value.count('\\n')
                            if comment_lines > 0:
                                line_no += comment_lines
                source_code = source_code[len(value):]
                break
        else:
            tokens.append(("Unexpected character", source_code[0], line_no))
            source_code = source_code[1:]
    return tokens

if __name__ == '__main__':
    with open("mySourceCode.txt", "r") as file:
        source_code = file.read()
    tokens = tokenize(source_code)
    for token_type, value, line_no in tokens:
        print([token_type, value, line_no])
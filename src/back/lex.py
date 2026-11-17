
import re

def lex(string: str):
    
    _tokens = re.split(r'(=|\+|-|\*|/|!|\(|\)|;|#|,|"| |\[|\])', string)

    STRING = False
    LIST = False
    COMMENT = False
    
    _STRING = ""
    _LIST = []

    tokens = []

    for token in _tokens:

        if token == '':
            continue

        if token == ' ':
            if STRING:
                _STRING += token
            continue

        if token == '#' and not STRING:
            COMMENT = not COMMENT
            continue

        if COMMENT:
            continue

        if token == '"':
            if not STRING:
                STRING = True
                _STRING = ""
            else:
                STRING = False

                if LIST:
                    _LIST.append(f'"{_STRING}"')
                else:
                    tokens.append(f'"{_STRING}"')

                _STRING = ""

            continue

        if STRING:
            _STRING += token
            continue

        if token == '[':
            LIST = True
            _LIST = []
            continue

        if token == ']':
            LIST = False
            tokens.append(_LIST)
            _LIST = []
            continue

        if LIST:
            if token != ',':
                _LIST.append(token)
        else:
            tokens.append(token)

    return tokens

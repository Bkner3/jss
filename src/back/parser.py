DEFAULT_COMMAND_LIST = ['let', 'const', 'is']
GLOBAL_COMMAND_LIST = [] #For fucntions and other stuff

def parse(tokens):
    if not tokens:
        return
    result = []

    for token in tokens:
        # Check if the token is a string literal
        if token.startswith('"') and token.endswith('"'):
            result.append({"type": "string", "value": token[1:-1]})

        # Check if the token is a number
        elif token.isdigit():
            result.append({"type": "number", "value": token})

        # Check if the token is an operator or a special character
        elif token in ['+', '-', '*', '/', '=', '(', ')', ';', '[', ']']:
            result.append({"type": "operator", "value": token})

        # Check if the token is a comment
        elif token == '#':
            result.append({"type": "comment", "value": token})

        # Check if the token is a command
        elif token in DEFAULT_COMMAND_LIST or token in GLOBAL_COMMAND_LIST:
            result.append({"type": "command", "value": token})
        # Check if the token is a variable (identifier)

        elif token.isalpha():
            result.append({"type": "variable", "value": token})

        else:
            result.append({"type": "unknown", "value": token})

    return result

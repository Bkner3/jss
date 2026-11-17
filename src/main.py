from src.input.read import read_file
from src.back.lex import lex
from src.back.parser import parse

def initialize():
    from src.input.arguments_parse import get_args
    args = get_args()
    main(args)

def main(args):

    if args.compile:
        pass
        source_code = read_file(args.compile)

    if args.run:
        _source_code = read_file(args.run)

        source_code = []

        for line in _source_code.splitlines():
            if not line.strip():
                continue
            lexed_code = lex(line)
            parsed_code = parse(lexed_code)
            
            if args.debug:
                print(lexed_code)
                print(parsed_code)
            source_code.append(parsed_code)




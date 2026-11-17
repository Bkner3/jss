import argparse

def get_args():
    parser = argparse.ArgumentParser(prog="jss", description="JSS - JavaScript Simplified")

    parser.add_argument("-c", "--compile", type=str, help="Compile a file.")
    parser.add_argument("-r", "--run", type=str, help="Run a file.")
    parser.add_argument("-d", "--debug", action="store_true", help="Debug a file.")

    parser.add_argument("-s", "--shell", action="store_true", help="Open the JSS shell.")
    parser.add_argument("-v", "--version", action="store_true", help="Show the version.")

    args = parser.parse_args()

    if not any(vars(args).values()):
        parser.print_help()
        parser.exit(1, "\nNo arguments provided.\n")

    return args

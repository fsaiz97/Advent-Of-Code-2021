import argparse


def parse_cli():
    parser = argparse.ArgumentParser()
    parser.add_argument('input', description="Takes the first cl argument as the input file.")
    return parser.parse_args()


def main():
    with open(args.input) as file:



if __name__ == '__main__':
    args = parse_cli()
    main()

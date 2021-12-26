import argparse


def parse_cli():
    parser = argparse.ArgumentParser()
    parser.add_argument('input', help="Takes the first cl argument as the input file.")
    return parser.parse_args()


def read_input(fn):
    with open(fn) as file:
        numbers = [int(x) for x in file.readline().strip().split(',')]
        _ = file.readline()

        for line in file:
            line = line.strip()
            

        boards = []
        while len(line) != 0:
            board = []
            for _ in range(5):
                board.append(file.readline)


def main():
    a = read_input(args.input)


if __name__ == '__main__':
    args = parse_cli()
    main()

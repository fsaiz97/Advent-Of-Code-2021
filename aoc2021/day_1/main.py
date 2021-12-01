import argparse
from itertools import pairwise


def parse_cli():
    parser = argparse.ArgumentParser()
    parser.add_argument('input', help="Takes the first command line argument as the input file.")
    return parser.parse_args()


def read_input():
    with open(args.input) as file:
        return [int(line.strip()) for line in file.readlines()]


def count_increases(sequence, window_size):
    start = 0
    stop = window_size - 1
    count = 0
    while stop < len(sequence) - 1:     # Prevents IndexError when getting the next number in the sequence
        if sequence[stop+1] > sequence[start]:
            # print(sequence[start], sequence[stop+1])  # debug
            count += 1
        start += 1
        stop += 1

    return count


def main():
    depths = read_input()
    pairs = pairwise(depths)
    count = len([pair for pair in pairs if pair[1] > pair[0]])

    print("Number of increases (Part 1) =", count)

    print("Number of increases (Part 2) =", count_increases(depths, 3))


if __name__ == '__main__':
    args = parse_cli()
    main()

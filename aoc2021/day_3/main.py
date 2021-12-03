import argparse


def parse_cli():
    parser = argparse.ArgumentParser()
    parser.add_argument('input', help="Takes the first cl argument as the input file.")
    return parser.parse_args()


def main():
    with open(args.input) as file:
        report = [list(line.strip()) for line in file.readlines()]

    n = len(report)
    # print(n)  # debug
    # print(report)  # debug
    z = zip(*report)

    counts = [item.count('1') for item in z]

    answer = [1 if count/n > 0.5 else 0 for count in counts]

    print(answer)


if __name__ == '__main__':
    args = parse_cli()
    main()

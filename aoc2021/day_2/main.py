import argparse


def parse_cli():
    parser = argparse.ArgumentParser()
    parser.add_argument('input', help="Takes the first cl argument as the input file.")
    return parser.parse_args()


def parse_input():
    with open(args.input) as file:
        lines = []
        for line in file:
            opcode, operand = line.strip().split()
            lines.append((opcode, int(operand)))

    return lines


def part_1(instructions):
    horizontal = 0
    depth = 0

    for opcode, operand in instructions:
        if opcode == 'forward':
            horizontal += operand
        elif opcode == 'down':
            depth += operand
        elif opcode == 'up':
            depth -= operand

    print("Part 1:")
    # print(f"{horizontal = }, {depth = }")
    print(f"{horizontal * depth = }")


def part_2(instructions):
    horizontal = 0
    depth = 0
    aim = 0

    for opcode, operand in instructions:
        if opcode == 'forward':
            horizontal += operand
            depth += aim * operand
        elif opcode == 'down':
            aim += operand
        elif opcode == 'up':
            aim -= operand

    print("Part 2:")
    # print(f"{horizontal = }, {depth = }")
    print(f"{horizontal * depth = }")


def main():
    instructions = parse_input()

    part_1(instructions)
    part_2(instructions)


if __name__ == '__main__':
    args = parse_cli()
    main()

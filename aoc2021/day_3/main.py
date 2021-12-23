import argparse
from statistics import mode as stat_mode

def parse_cli():
    parser = argparse.ArgumentParser()
    parser.add_argument('input', help="Takes the first cl argument as the input file.")
    return parser.parse_args()


def list_to_bin(digits):
    return sum(d << i for i, d in enumerate(reversed(digits)))


def mode(digits):
    return None if digits.count(1) == digits.count(0) else stat_mode(digits)


def check_bit_criteria_mc(binary, count, i, n):
    if count/n > 0.5 and binary[i]:
        return True
    elif count/n < 0.5 and not binary[i]:
        return True
    elif count/n == 0.5 and binary[i]:
        return True
    else:
        return False

def check_bit_criteria(bit, common, setting):
    # checks if the bit meets the bit criteria according to the setting.
    result = bool(bit) if common == None else not (bit ^ common)

    if setting == "mc":
        return result
    elif setting == "lc":
        return not result
    else:
        ValueError("Setting does not exist.")


def part_2_alg(report, n, setting):
    for i in range(n):
        common = mode([x[i] for x in report])
        temp = [x for x in report if check_bit_criteria(x[i], common, setting)]
        report = temp.copy()

        if len(report) == 1:
            return list_to_bin(report[0])

    return None


def main():
    with open(args.input) as file:
        report = [[int(d) for d in line.strip()] for line in file.readlines()]

    n = len(report[0])

    gamma = list_to_bin(list(map(mode, zip(*report))))

    mask = sum(1 << i for i in range(n))

    epsilon = mask ^ gamma

    print(f"Power consumption = {gamma * epsilon}")

    oxy = part_2_alg(report, n, 'mc')
    co2 = part_2_alg(report, n, 'lc')

    lf_supp = oxy * co2
    print(f"{lf_supp = }")


if __name__ == '__main__':
    args = parse_cli()
    main()


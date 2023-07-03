MAX_DEPTH = 1024


def pascal_value_for(row, i):
    if i == 0:
        return row[0]
    if i == len(row):
        return row[-1]
    return row[i-1] + row[i]


def pascal(row):
    return [pascal_value_for(row, i) for i in range(len(row) + 1)]


def find_powers_of_two(row):
    power_found = False
    powers = []
    total = row[0]  # ignore 1 = 2⁰
    for i in range(1, len(row)):
        total += row[i]
        if bin(total).count("1") == 1:
            power_found = True
            powers.append((i, total))
    return power_found, powers


if __name__ == '__main__':
    row = [1]
    powers_by_row = dict()
    powers_list = []
    for i in range(MAX_DEPTH):
        row = pascal(row)
        power_found, powers = find_powers_of_two(row)
        if power_found:
            powers_by_row[i] = powers
            for power in powers:
                powers_list.append((i, power))

    for power in powers_list:
        print(f"{power[0]}\t{power[1][0]}\t{power[1][1]}")


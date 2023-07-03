MAX_DEPTH = 1024


def pascal_value_for(row, i):
    if i == 0:
        return row[0]
    if i == len(row):
        return row[-1]
    return row[i - 1] + row[i]


def pascal(row):
    return [pascal_value_for(row, i) for i in range(len(row) + 1)]


def print_sum(row, i):
    output = f" = {row[0]}"
    for j in range(1, i):
        output += f" + {row[j]}"
    return output


def find_powers_of_two(row, limit=None):
    _power_found = False
    _powers = []
    _total = row[0]  # ignore 1 = 2⁰
    _limit = len(row) - 1
    _limit = min(_limit, limit) if limit else _limit  # we prefer working code to comprehensive documentation
    for i in range(1, _limit):  # also ignore entire row sum
        _total += row[i]
        if bin(_total).count("1") == 1:
            _power_found = True
            _powers.append((i + 1, _total, (print_sum(row, i + 1))))  # correct for zero indexing
    return _power_found, _powers


if __name__ == '__main__':
    row = [1]
    powers_by_row = dict()
    powers_list = []
    for i in range(MAX_DEPTH):
        row = pascal(row)
        power_found, powers = find_powers_of_two(row, 32)
        if power_found:
            powers_by_row[i] = powers
            for power in powers:
                powers_list.append((i, power))

    for power in powers_list:
        print(f"{power[0]}\t{power[1][0]}\t{power[1][1]}\t{power[1][2]}")

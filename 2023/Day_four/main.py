d = open("input.txt", "r").read().strip()
lines = d.split('\n')


# Part 1
def part_one():
    score = 0
    for line in lines:
        winners, rest = line.split('|')
        id_, card = winners.split(':')
        win_nums = [int(x) for x in card.split()]
        card_nums = [int(x) for x in rest.split()]
        matching_nums = len(list(set(card_nums).intersection(win_nums)))
        if matching_nums > 0:  # First matching point is worth 1, every point following is worth double
            score += 2 ** (matching_nums - 1)

    print(score)


def part_two():
    from collections import defaultdict
    score = 0
    h = defaultdict(int)
    for i, line in enumerate(lines):
        h[i] += 1
        winners, rest = line.split('|')
        id_, card = winners.split(':')
        win_nums = [int(x) for x in card.split()]
        card_nums = [int(x) for x in rest.split()]
        matching_nums = len(list(set(card_nums).intersection(win_nums)))
        if matching_nums > 0:  # First matching point is worth 1, every point following is worth double
            score += 2 ** (matching_nums - 1)
        for j in range(matching_nums):
            h[i + 1 + j] += h[i]
    print(sum(h.values()))


if __name__ == "__main__":
    # part_one()
    part_two()

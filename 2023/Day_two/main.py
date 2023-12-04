d = open("prompt.txt", "r").read().strip()

# Part 1
def part_one():
    ans = 0
    for line in d.split('\n'):
        ok = True
        id_, line = line.split(':')
        for event in line.split(';'):
            for balls in event.split(','):
                n, color = balls.split()
                if int(n) > {'red': 12, 'green': 13, 'blue': 14}.get(color, 0):
                    ok = False
        if ok:
            ans += int(id_.split()[-1])
            print(id_)
    print(ans)


# Part 2
def part_two():
    from collections import defaultdict
    ans = 0
    for line in d.split('\n'):
        ok = True
        id_, line = line.split(':')
        V = defaultdict(int)
        for event in line.split(';'):
            for balls in event.split(','):
                n, color = balls.split()
                n = int(n)
                V[color] = max(V[color], n)
                if int(n) > {'red': 12, 'green': 13, 'blue': 14}.get(color, 0):
                    ok = False
        print(V)
        score = 1
        for v in V.values():
            score *= v
        ans += score
    print(ans)


if __name__ == "__main__":
    # part_one()
    part_two()
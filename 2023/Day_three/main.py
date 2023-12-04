
d = open('prompt.txt', 'r').read().strip()
lines = d.split('\n')


# part one
def part_one():
    for line in lines:
        print(line)


if __name__ == "__main__":
    part_one()

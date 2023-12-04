
def part_one():
    p = open("Prompt.txt", "r").read().strip()
    answer = 0

    for line in p.split('\n'):
        digits = []
        for c in line:
            if c.isdigit():
                digits.append(c)
        score = int(digits[0] + digits[-1])
        answer += score

    print(answer)

def part_two():
    p = open("Prompt.txt", "r").read().strip()
    answer = 0

    for line in p.split('\n'):
        digits = []
        for i, c in enumerate(line):
            if c.isdigit():
                digits.append(c)
            for d, val in enumerate(['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']):
                if line[i:].startswith(val):
                    digits.append(str(d + 1))
        score = int(digits[0] + digits[-1])
        answer += score

    print(answer)

if __name__ == "__main__":
    part_one()
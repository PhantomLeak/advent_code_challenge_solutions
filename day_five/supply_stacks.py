
# Numeric values telling which rows to move to which row and how many crates to move to new row
line_numbers = [[int(x) for x in line.split() if x.isdigit()] for line in open("day_five/input.txt").read().split("\n") if line.startswith("move")]

# Letters representing crates in the stacks
letter_stacks = [[r[k] for r in [line[1::4] for line in open("day_five/input.txt").read().split("\n") if "[" in line] if r[k] != " "] for k in range(9)]

z = letter_stacks[:]
for i in line_numbers:
    # Get numbers of which stack starting, amount moving and how many are being moved
    # a: row number, f: number from stack after being moved too , t: number from stack being moved
    a, f, t = i[0], i[1] - 1, i[2] - 1
    
    letter_stacks[t] = letter_stacks[f][:a][::-1] + letter_stacks[t]
    letter_stacks[f] = letter_stacks[f][a:]

    z[t] = z[f][:a] + z[t]
    z[f] = z[f][a:]

print(f'Part One: {"".join(x[0]for x in letter_stacks)}')
print(f'Part Two: {"".join(x[0]for x in z)}')


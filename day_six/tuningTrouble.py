
with open('day_six/input.txt') as file:
    data = file.readline()

# Part one had a length of 4, part two is 14
markLength = 14
letters = [' '] * markLength
index = 0

for letter in data:
    index += 1
    # Break letters into lists with the mark length
    letters = letters[1:]
    letters.append(letter)
    # Check if the set of letters is distinct if so then that's our marker
    if len(set(letters)) == markLength and letters[0] != ' ':
        print(f'Solution: {index}')
        break
def part_one():
    data = []
    with open('day_three/input.txt', 'r') as f:
        for lines in f.readlines():
            for item in lines.strip().split(' '):
                data.append(item)
    
    score = 0
    for bag in data:
        first_half = sorted(bag[:len(bag)//2]) # Sort the string for the first half
        a = []
        [a.append(x) for x in first_half if x not in a]

        second_half = sorted(bag[len(bag)//2:]) # Sort the string for the second half
        b = []
        [b.append(x) for x in second_half if x not in b]

        for character in a:
            if character in b:
                if character >= 'a' and character <= 'z':
                    score += (ord(character) - 96) # Ord returns an int representation of the unicode character (ex. p = 80)
                if character >= 'A' and character <= 'Z':
                    score += (ord(character) - 38)
        
    print(score)


def part_two():
    data = []
    with open('day_three/input.txt', 'r') as f:
        for lines in f.readlines():
            for item in lines.strip().split(' '):
                data.append(item)
    
    score = 0
    for index in range(len(data)//3):
        aa = sorted(data[index*3])
        a = []
        [a.append(x) for x in aa if x not in a]

        bb = sorted(data[3*index+1])
        b = []
        [b.append(x) for x in bb if x not in b]

        cc = sorted(data[3*index+2])
        c = []
        [c.append(x) for x in cc if x not in c]

        for character in a:
            if character in b:
                if character in c:
                    if character >= 'a' and character <= 'z':
                        score += (ord(character) - 96) # Ord returns an int representation of the unicode character (ex. p = 80)
                    if character >= 'A' and character <= 'Z':
                        score += (ord(character) - 38)
    print(score)

part_two()
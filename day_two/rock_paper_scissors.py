
def part_one():
    data = []
    with open('day_two/input.txt', 'r') as f:
        for lines in f.readlines():
            elements = []
            for items in lines.strip().split(' '):
                elements.append(items)
            data.append(elements)
    
    # --- Point system ---
    '''
        Rock = 1, Paper = 2, Scissors = 3
        Lose = 0, Tie = 3, Win = 6
    '''

    # --- Game System ---
    '''
        A = Rock, B = Paper, C = Scissors
        X = Rock, Y = Paper, Z = Scissors
    '''
    total_score = 0

    for lines in data:
        if lines[1] == 'X': # Rock
            total_score += 1
        if lines[1] == 'Y': # Paper
            total_score += 2
        elif lines[1] == 'Z': # Scissors
            total_score += 3
        
        # If win
        if (lines[0] == 'B' and lines[1] == 'Z') or (lines[0] == 'A' and lines[1] == 'Y') or (lines[0] == 'C' and lines[1] == 'X'):
            total_score += 6
        # If tie
        if (lines[0] == 'A' and lines[1] == 'X') or (lines[0] == 'B' and lines[1] == 'Y') or (lines[0] == 'C' and lines[1] == 'Z'):
            total_score += 3
        
    print(total_score)


def part_two():
    data = []
    with open('day_two/input.txt', 'r') as f:
        for lines in f.readlines():
            elements = []
            for items in lines.strip().split(' '):
                elements.append(items)
            data.append(elements)

    total_score = 0

    options = {tuple(['A', 'X']): 3, tuple(['A', 'Y']): 4, tuple(['A', 'Z']): 8,  tuple(['B', 'X']): 1, 
    tuple(['B', 'Y']): 5, tuple(['B', 'Z']): 9,  tuple(['C', 'X']): 2, tuple(['C', 'Y']): 6, 
    tuple(['C', 'Z']): 7}
    
    total_score = sum([options[tuple(lines)] for lines in data])

    print(total_score)

part_two()
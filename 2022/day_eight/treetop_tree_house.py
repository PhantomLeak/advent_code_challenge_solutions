data = []
with open('day_eight/input.txt') as file:
    for line in file.readlines():
        data.append(line.strip())

trees = 0

# Movments (left, right, down, up)
movements = [[1,0], [-1,0], [0,-1], [0,1]]

for x in range(len(data)):
    for y in range(len(data[x])):
        for i in range(4): # Only four possible movement options
            xx = x + movements[i][0]
            yy = y + movements[i][1]
            
            #Specifc 'tree' for testing
            h = int(data[x][y])

            tallest = True
            
            while (xx >= 0 and xx < len(data)) and (yy >= 0 and yy < len(data[x])):
                # If this tree being compared to the tree were testing is taller, set tallest false and break loop
                if int(data[xx][yy]) >= h:
                    tallest = False 
                    break
                xx += movements[i][0]
                yy += movements[i][1]

            # If the tree turns out to be the tallest then add it to a possible tree for the treehouse
            if tallest:
                trees += 1
                break

print(f'Part 1 Solution: {trees}')


# Part Two find the highest scenic score possible 

# Movments (left, right, down, up)
movements = [[1,0], [-1,0], [0,-1], [0,1]]
max_score = 0

for x in range(len(data)):
    for y in range(len(data[x])):
        score = 1
        
        for i in range(4): # Only four possible movement options
            xx = x + movements[i][0]
            yy = y + movements[i][1]
            
            #Specifc 'tree' for testing
            h = int(data[x][y])

            moves = 0
            
            while (xx >= 0 and xx < len(data)) and (yy >= 0 and yy < len(data[x])):
                moves += 1
                # If this tree being compared to the tree were testing is taller, set tallest false and break loop
                if int(data[xx][yy]) >= h:
                    break

                xx += movements[i][0]
                yy += movements[i][1]
            score *= moves
            # Find if the new score is higher than the previous max...If it is, replace it 
        max_score = max(max_score, score)

print(f'Part 2 Solution: {max_score}')
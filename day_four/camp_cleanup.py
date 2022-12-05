def part_one():
    data = []
    with open('day_four/input.txt', 'r') as f:
        # Clean up data into clean list of lists
        for lines in f.readlines():
            element = []
            for item in lines.strip().split(','):
                item = item.split('-')
                element.append(item)
            data.append(element)

    full_contain = 0
    partial = 0
    for lines in data:
        a = int(lines[0][0]) # first list first item
        b = int(lines[0][1]) # first list second item
        c = int(lines[1][0]) # second list first item
        d = int(lines[1][1]) # second list second item
        # first range contains second range
        if a >= c and b <= d:
            full_contain += 1
        # second range contains first range
        elif c >= a and d <= b:
            full_contain += 1
        # If both ranges partially contain eachother
        if b >= c and d >= a:
            partial += 1
    
    print(f'Fully contain: {full_contain}')
    print(f'Partially contain: {partial}')
    

part_one()
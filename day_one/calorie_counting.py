# This challenge is to take a massive list of numbers and calculate which sum is the greatest

# Read 'input' items from the txt file
def part_one():
    with open('day_one/input.txt', 'r') as f:
        lines = f.readlines()

    max_result = 0
    cur_results = 0
    for el in lines:
        if el != '\n': # If the line isn't blank
            cur_results += int(el)# Sum results (grouped items)
        else: # If there is a blank line
            if cur_results > max_result: # If the current results are greater than the previous max 
                max_result = cur_results
            cur_results = 0

    print(max_result)

# In this section, they want to know the top three elves carrying the most calories
def part_two():
    with open('day_one/input.txt', 'r') as f:
        lines = f.readlines()
    
    elf_one, elf_two, elf_three = 0, 0, 0
    cur_results = 0
    for el in lines:
        if el != '\n': # If line isn't blank
            cur_results += int(el) # Sum results (grouped items)
        else:
            if cur_results > elf_three:
                if cur_results < elf_two:
                    elf_three = cur_results
                elif cur_results < elf_one:
                    elf_two, elf_three = cur_results, elf_two
                else:
                    elf_one, elf_two, elf_three = cur_results, elf_one, elf_two
            cur_results = 0
    
    print(sum([elf_one, elf_two, elf_three]))


part_two()
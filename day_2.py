def get_direction(contents):
    if contents[0] > contents[1]:
        direction = -1
    elif contents[0] < contents[1]:
        direction = 1
    else:
        direction = 0
    return(direction)

def check_safety(item1, item2, direction):
    diff = (item2 - item1) * direction
    if diff <= 3 and diff >= 1:
        return True
    else:
        return False

def check_all_safety(list):
    direction = get_direction(list)
    safe = True
    j = 0
    while safe == True and j < (len(list) - 1):
        safe = check_safety(list[j], list[j+1], direction)
        j += 1
    return(safe)

#Part 1
total_safety = 0
with open("Inputs/Input day 2", "r") as input_file:
    for line in input_file:
        contents = [int(i) for i in line.split()]
        total_safety += check_all_safety(contents)

print(total_safety)
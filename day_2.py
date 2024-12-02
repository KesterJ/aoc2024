def get_single_direction(x, y):
    if x > y:
        direction = -1
    elif x < y:
        direction = 1
    else:
        direction = 0
    return(direction)

def get_direction(contents):
    three_dirs = [get_single_direction(contents[i], contents[i+1]) for i in range(0, 3)]
    if three_dirs[0] == three_dirs[1]:
        return three_dirs[0]
    elif three_dirs[0] == three_dirs[2]:
        return three_dirs[0]
    elif three_dirs[1] == three_dirs[2]:
        return three_dirs[1]
    else:
        return 99

def check_safety(item1, item2, direction):
    diff = (item2 - item1) * direction
    if diff <= 3 and diff >= 1:
        return True
    else:
        return False

def check_all_safety(list, tolerance = False):
    direction = get_direction(list)
    safe = False if direction == 99 else True
    j = 0
    found_error = False
    while safe == True and j < (len(list) - 1):
        safety = check_safety(list[j], list[j+1], direction)
        if not safety:
            if found_error or not tolerance:
                safe = False
            else:
                found_error = True
            if j < len(list) - 2:
                can_skip = check_safety(list[j], list[j+2], direction)
                if can_skip:
                    j += 1
                elif j > 0:
                    safe = False
        j += 1
    return(safe)

#Part 1
total_safety = 0
with open("Inputs/Input day 2", "r") as input_file:
    for line in input_file:
        contents = [int(i) for i in line.split()]
        total_safety += check_all_safety(contents)

print(total_safety)

#Part 2
total_safety_2 = 0
with open("Inputs/Input day 2", "r") as input_file:
    for line in input_file:
        contents = [int(i) for i in line.split()]
        total_safety_2 += check_all_safety(contents, tolerance = True)

print(total_safety_2)
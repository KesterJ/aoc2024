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

def check_all_safety(list, tolerance):
    direction = get_direction(list)
    safe = True
    j = 0
    current_errors = 0
    while safe == True and j < (len(list) - 1) and current_errors <= tolerance:
        safety = check_safety(list[j], list[j+1], direction)
        if not safety:
            if current_errors == tolerance:
                safe = False
            else:
                current_errors += 1
            if j < len(list) - 2 and check_safety(list[j], list[j+2], direction):
                j += 1
        j += 1
    return(safe)

#Part 1
total_safety = 0
with open("Inputs/Input day 2", "r") as input_file:
    for line in input_file:
        contents = [int(i) for i in line.split()]
        total_safety += check_all_safety(contents, tolerance = 0)

print(total_safety)

#Part 2
total_safety_2 = 0
with open("Inputs/Input day 2", "r") as input_file:
    for line in input_file:
        contents = [int(i) for i in line.split()]
        total_safety_2 += check_all_safety(contents, tolerance = 1)

print(total_safety_2)
with open('Inputs/Input day 4', 'r') as input_file:
    grid = input_file.readline().rstrip('\n')
    line_length = len(grid)
    for line in input_file:
        grid += line.rstrip('\n')

#Define a single step in each direction starting clockwise from north
directions = [-line_length, 1-line_length, 1, 1+line_length, line_length, line_length-1, -1, -(line_length+1)]

starting_xs = []
for direction in directions:
    xmases = [index for index, character in enumerate(grid)
              if (character == "X" and (abs(index % line_length - (index + 3*direction) % line_length)) <= 3 and
              index + 3*direction >= 0 and index + 3*direction <= len(grid) and
              grid[index + direction] == "M" and grid[index + 2*direction] == "A" and
              grid[index + 3*direction] == "S")]
    starting_xs.append(xmases)

answer = sum([len(x) for x in starting_xs])

#Part 2
def m_or_s(index):
    if grid[index] == "M":
        return 1
    elif grid[index] == "S":
        return 2
    else:
        return 0
    
x_mases = [index for index, character in enumerate(grid)
           if index % line_length not in [0, line_length - 1] and
           index >= line_length and index < len(grid) - line_length and
           character == "A" and
           m_or_s(index + line_length + 1) + m_or_s(index - line_length - 1) == 3 and
           m_or_s(index - line_length + 1) + m_or_s(index + line_length - 1) == 3]
    
answer_2 = len(x_mases)
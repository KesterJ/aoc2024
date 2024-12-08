from itertools import combinations

def get_antenna_locations(grid):
    antenna_dict = {}
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            current_char = grid[i][j]
            if current_char != '.':
                if current_char in antenna_dict:
                    antenna_dict[current_char].append([i,j])
                else:
                    antenna_dict[current_char] = [[i,j]]
    return(antenna_dict)

def find_single_antinodes(dict, height, width):
    antinodes = []
    for key in dict:
       for combn in combinations(dict[key], 2):
           antinodes.append((2 * combn[0][0] - combn[1][0], 2 * combn[0][1] - combn[1][1]))
           antinodes.append((2 * combn[1][0] - combn[0][0], 2 * combn[1][1] - combn[0][1]))
    antinodes = list(set(antinodes))
    antinodes = [antinode for antinode in antinodes if (antinode[0] >= 0 and
                                                        antinode[0] < height and
                                                        antinode[1] >= 0 and
                                                        antinode[1] < width)]
    return(antinodes)                               

def find_all_antinodes(dict, height, width):
    antinodes = []
    for key in dict:
       for combn in combinations(dict[key], 2):
           x_step = combn[1][0] - combn[0][0]
           y_step = combn[1][1] - combn[0][1]
           if x_step > 0:
               x_forward = (height - combn[0][0] - 1) // x_step
               x_back = combn[0][0] // x_step
           elif x_step < 0:
               x_forward = combn[0][0] // -x_step
               x_back = (height - combn[0][0] - 1) // -x_step
           else:
               #Should technically be inf but any high value should be fine  
               x_forward = height + 1
               x_back = height + 1
           if y_step > 0:
               y_forward = (width - combn[0][1] - 1) // y_step
               y_back = combn[0][1] // y_step
           elif y_step < 0:
               y_forward = combn[0][1] // -y_step
               y_back = (width - combn[0][1] - 1) // -y_step
           else:
               #Should technically be inf but any high value should be fine  
               y_forward = height + 1
               y_back = height + 1         
           steps_forward = min(x_forward, y_forward)
           steps_back = min(x_back, y_back)
           forwards = [(combn[0][0] + i*x_step, combn[0][1] + i*y_step) for i in range(0, steps_forward + 1)]
           backwards = [(combn[0][0] - i*x_step, combn[0][1] - i*y_step) for i in range(1, steps_back + 1)]
           antinodes = antinodes + forwards + backwards
    antinodes = list(set(antinodes))
    return(antinodes) 

def solver(grid, all = False):
    width = len(grid[0])
    height = len(grid)
    antennas = get_antenna_locations(grid)
    if all:
        antinodes = find_all_antinodes(antennas, height, width)
    else:
        antinodes = find_single_antinodes(antennas, height, width)
    return(antinodes)

with open('Inputs/Input day 8', 'r') as input_file:
    lines = input_file.readlines()
    lines = [line.rstrip('\n') for line in lines]
    
antinodes = solver(lines)
answer = len(antinodes)

all_antinodes = solver(lines, all = True)
answer_2 = len(all_antinodes)
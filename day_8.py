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

def find_antinodes(dict, height, width):
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

def solver(grid):
    width = len(grid[0])
    height = len(grid)
    antennas = get_antenna_locations(grid)
    antinodes = find_antinodes(antennas, height, width)
    return(antinodes)

with open('Inputs/Input day 8', 'r') as input_file:
    lines = input_file.readlines()
    lines = [line.rstrip('\n') for line in lines]
    
antinodes = solver(lines)
answer = len(antinodes)    
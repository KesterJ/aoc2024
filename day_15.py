import numpy as np
import copy

def parse_input(input_lines):
    lines = [line.rstrip('\n') for line in input_lines]
    split = [len(line) for line in lines].index(0)
    icon_dict = {'#': -1, '.': 0, 'O': 1, '@': 2}
    map = np.array([[icon_dict[character] for character in list(line)] for line in lines[:split]])
    robot_position = np.where(map == 2)
    robot_position = [robot_position[0][0], robot_position[1][0]]
    map[tuple(robot_position)] = 0
    instruction_dict = {'<': {"axis": 1, "dir": -1}, '>': {"axis": 1, "dir": 1},
                        '^': {"axis": 0, "dir": -1}, 'v': {"axis": 0, "dir": 1}}
    instructions = [instruction_dict[char] for char in ''.join(lines[split+1:])]
    return (map, robot_position, instructions)

def move_robot(inputs):
    
    def test_push(pos, instruction):
        current_pos = copy.deepcopy(pos)
        while map[tuple(current_pos)] == 1:
            current_pos[instruction["axis"]] += instruction["dir"] 
        if map[tuple(current_pos)] == -1:
            return (False, -1)
        elif map[tuple(current_pos)] == 0:
            return(True, current_pos)
    
    map = inputs[0]
    robot_position = inputs[1]
    instructions = inputs[2]
    for j, instruction in enumerate(instructions):
        new_pos = copy.deepcopy(robot_position)
        new_pos[instruction["axis"]] += instruction["dir"]
        if map[tuple(new_pos)] == 0:
            robot_position = new_pos
        elif map[tuple(new_pos)] == 1:
            push = test_push(new_pos, instruction)
            if push[0]:
                map[tuple(push[1])] = 1
                map[tuple(new_pos)] = 0
                robot_position = new_pos
        print(robot_position[0], robot_position[1], j)
    return(map)

def get_score(new_map):
    total = 0
    for i in range(0, new_map.shape[0]):
        for j in range(0, new_map.shape[1]):
            if new_map[i,j] == 1:
                total += 100*i
                total += j
    return total

with open('Inputs/Input day 15', 'r') as input_file:
    lines = input_file.readlines()

inputs = parse_input(lines)
new_map = move_robot(inputs)
answer = get_score(new_map)
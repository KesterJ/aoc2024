from re import findall
import numpy as np
import copy
from matplotlib import pyplot as plt

def process_line(line):
    matches = findall("(-?\d+)", line)
    dict = {"x_pos": int(matches[0]), "y_pos": int(matches[1]), "x_vel": int(matches[2]), "y_vel": int(matches[3])}
    return(dict)

def move_robots(robots, times, width, height):
    for robot in robots:
        robots[robot]["x_pos"] = (robots[robot]["x_pos"] + (robots[robot]["x_vel"] * times)) % width
        robots[robot]["y_pos"] = (robots[robot]["y_pos"]  + (robots[robot]["y_vel"] * times)) % height
    return(robots)

def find_quadrant(robot, width, height):
    if robot["x_pos"] < width // 2:
        x_quad = 0
    elif robot["x_pos"] > width // 2:
        x_quad = 1
    else:
        x_quad = -100
    if robot["y_pos"] < height // 2:
        y_quad = 0
    elif robot["y_pos"] > height // 2:
        y_quad = 2
    else:
        y_quad = -100
    quadrant = max(-1, x_quad + y_quad)
    return(quadrant)

def get_answer(quadrants):
    totals = [sum([1 for quadrant in quadrants if quadrant == i]) for i in range(0, 4)]
    product = 1
    for total in totals:
        product *= total
    return(product)

with open('Inputs/Input day 14', 'r') as input_file:
    lines = input_file.readlines()
    robot_dict = {i: process_line(line) for i, line in enumerate(lines)}

width = 101
height = 103
move_robots(robot_dict, times = 100, width = width, height = height)
quadrants = [find_quadrant(robot_dict[robot], width = width, height = height) for robot in robot_dict]
answer_1 = get_answer(quadrants)

#Part 2
def check_quadrants(times):
    quad_totals = []
    for tick in range(1, times + 1):
        move_robots(robot_dict, times = 1, width = width, height = height)
        quadrants = [find_quadrant(robot_dict[robot], width = width, height = height) for robot in robot_dict]
        quad_totals.append(get_answer(quadrants))
    return quad_totals

def visualise_positions(robot_dict):
    locations = np.zeros([width, height])
    for robot in robot_dict:
        locations[robot_dict[robot]["x_pos"], robot_dict[robot]["y_pos"]] += 1
    plt.matshow(locations)

with open('Inputs/Input day 14', 'r') as input_file:
    lines = input_file.readlines()
    robot_dict = {i: process_line(line) for i, line in enumerate(lines)}

backup_robots = copy.deepcopy(robot_dict)

width = 101
height = 103   
quads = check_quadrants(times = 10403)

least_balanced = quads.index(min(quads))
move_robots(backup_robots, times = least_balanced + 1, width = width, height = height)
visualise_positions(backup_robots)

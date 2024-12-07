from datetime import datetime

def cat_numbers(num1, num2):
    return(int(str(num1) + str(num2)))

def carol(problem, concatenation = False):
    total = problem[0]
    numbers = problem[1]
    #Check once we have only two numbers
    if len(numbers) == 2:
        if (numbers[0] * numbers[1] == total or
            numbers[0] + numbers[1] == total or
            (concatenation == True and cat_numbers(numbers[1], numbers[0]) == total)):
            return(True)
        else:
            return(False)
    #Check concatenation
    total_str = str(total)
    current_str = str(numbers[0])
    if concatenation == True and len(total_str) > len(current_str) and total_str[-len(current_str):] == current_str:
        with_concat = carol([int(total_str[:-len(current_str)]), numbers[1:]], concatenation = concatenation)
        if with_concat:
            return(True)
    #Check factorisation
    if total % numbers[0] == 0:
        with_multiply = carol([total // numbers[0], numbers[1:]], concatenation = concatenation)
        if with_multiply:
            return(True)
    if numbers[0] < total:
        with_add = carol([total - numbers[0], numbers[1:]], concatenation = concatenation)
        if with_add:
            return(True)
    return False

with open('Inputs/Input day 7', 'r') as input_file:
    inputs = input_file.readlines()
    inputs = [input.rstrip('\n') for input in inputs]
    problems = [[int(input.split(':')[0]), [int(x) for x in input.split(':')[1].split(' ')[1:]]]
                for input in inputs]

#Prep
for i in range(0, len(problems)):
    problems[i][1].reverse()

answer = sum([problem[0] for problem in problems if carol(problem)])
print(datetime.now())
answer_2 = sum([problem[0] for problem in problems if carol(problem, concatenation = True)])
print(datetime.now())
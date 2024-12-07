def carol(problem):
    total = problem[0]
    numbers = problem[1]
    #Check once we have only two numbers
    if len(numbers) == 2:
        if numbers[0] * numbers[1] == total or numbers[0] + numbers[1] == total:
            return(True)
        else:
            return(False)
    #Otherwise check factorisation and do appropriate checks
    if total % numbers[0] != 0:
        return carol([total - numbers[0], numbers[1:]])
    else:
        result = (carol([total / numbers[0], numbers[1:]]) or
                  carol([total - numbers[0], numbers[1:]]))
        return result

with open('Inputs/Input day 7', 'r') as input_file:
    inputs = input_file.readlines()
    inputs = [input.rstrip('\n') for input in inputs]
    problems = [[int(input.split(':')[0]), [int(x) for x in input.split(':')[1].split(' ')[1:]]]
                for input in inputs]

#Prep
for i in range(0, len(problems)):
    problems[i][1].reverse()

answer = sum([problem[0] for problem in problems if carol(problem)])

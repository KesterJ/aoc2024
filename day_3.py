from re import findall

def multiply_tuples(mul_list):
    products = [int(i[0]) * int(i[1]) for i in mul_list]
    return sum(products)

running_total = 0
all_muls = []
with open('Inputs/Input day 3', 'r') as input_file:
    for line in input_file:
        muls = findall(r'mul\((\d+),(\d+)\)', line)
        running_total += multiply_tuples(muls)
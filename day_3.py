from re import findall, finditer

def product_tuple(matched_tuple):
    return(int(matched_tuple[0]) * int(matched_tuple[1]))

def multiply_tuples(mul_list):
    products = [product_tuple(i) for i in mul_list]
    return sum(products)

def parse_matches(line, enabled):
    total = 0
    for i in finditer(r'mul\((\d+),(\d+)\)|do\(\)|don\'t\(\)', line):
        if i.group() == 'do()':
            enabled = True
        elif i.group() == 'don\'t()':
            enabled = False
        elif enabled:
            total += product_tuple(i.groups())
    return dict(total = total, enabled = enabled)

#Part 1
running_total = 0
with open('Inputs/Input day 3', 'r') as input_file:
    for line in input_file:
        muls = findall(r'mul\((\d+),(\d+)\)', line)
        running_total += multiply_tuples(muls)
        
print(running_total)
        
#Part 2
running_total = 0
enabled = True
with open('Inputs/Input day 3', 'r') as input_file:
    for line in input_file:
        parsed = parse_matches(line, enabled)
        running_total += parsed['total']
        enabled = parsed['enabled']

print(running_total)
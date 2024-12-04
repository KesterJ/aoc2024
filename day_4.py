def char_indices(char, string):
    indices = []
    for index, character in enumerate(string):
        if character == char:
            indices.append(index)
    return(indices)

with open('Inputs/Input day 4', 'r') as input_file:
    firstline = input_file.readline().rstrip('\n')
    line_length = len(firstline)
    x_indices = char_indices('X', firstline)
    m_indices = char_indices('M', firstline)
    a_indices = char_indices('A', firstline)
    s_indices = char_indices('S', firstline)
    line_pos = 1
    for line in input_file:
        x_indices += [i + line_pos*line_length for i in char_indices('X', line)]
        m_indices += [i + line_pos*line_length for i in char_indices('M', line)]
        a_indices += [i + line_pos*line_length for i in char_indices('A', line)]
        s_indices += [i + line_pos*line_length for i in char_indices('S', line)]
        line_pos += 1
        
#Define a single step in each direction starting clockwise from north
directions = [-line_length, 1-line_length, 1, 1+line_length, line_length, line_length-1, -1, -(line_length+1)]
          
starting_xs = []
for direction in directions:
    xmases = [index for index in x_indices if (index + direction in m_indices and
                                               index + 2*direction in a_indices and
                                               index + 3*direction in s_indices and
                                               (abs(index % line_length - (index + 3*direction) % line_length)) <= 3)]
    starting_xs.append(xmases)

answer = sum([len(x) for x in starting_xs])

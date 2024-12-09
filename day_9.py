
def unpack_file(file):
    unpacked = [[i//2]*int(file[i]) if i % 2 == 0 else [-1]*int(file[i]) for i in range(0, len(file))]
    flattened = [i for sublist in unpacked for i in sublist]
    return(flattened)

def rearrange_files(disk):
    start = 0
    end = len(disk) - 1
    while start < end:
        while disk[start] != -1:
            start += 1
        while disk[end] == -1:
            end -= 1
        if start < end:
            disk[start] = disk[end]
            disk[end] = -1
    return(disk)
   

with open('Inputs/Input day 9', 'r') as input_file:
    input = [line.rstrip('\n') for line in input_file.readlines()]
    input = ''.join(input)

full_file = unpack_file(input)
rearranged = rearrange_files(full_file)
checksum = sum([i * rearranged[i] for i in range(0, len(rearranged)) if rearranged[i] != -1])


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

with open('Inputs/Example day 9', 'r') as input_file:
    input = [line.rstrip('\n') for line in input_file.readlines()]
    input = ''.join(input)

full_file = unpack_file(input)
rearranged = rearrange_files(full_file)
checksum = sum([i * rearranged[i] for i in range(0, len(rearranged)) if rearranged[i] != -1])

#Part 2
def get_compressed_file(file):
    compressed = [[i//2, int(file[i])] if i % 2 == 0 else [-1, int(file[i])] for i in range(0, len(file))]
    return(compressed)

def rearrange_chunks(disk_repr):
    for i in reversed(range(0, (len(disk_repr) // 2) + 1)):
        #Find right chunk
        for j, chunk in enumerate(disk_repr):
            if chunk[0] == i:
                location = j
        item_len = disk_repr[location][1]
        #Find space
        k = 0
        found = False
        space_loc = -1
        while found == False and k < location:
            if disk_repr[k][0] == -1 and disk_repr[k][1] >= disk_repr[location][1]:
                found = True
                space_loc = k
            k += 1
        space_len = disk_repr[space_loc][1] if found else 0
        #Swap
        if found and space_len == item_len:
            disk_repr[space_loc] = disk_repr[location]
            disk_repr[location] = [-1, item_len]
        elif found:
            diff = space_len - item_len
            disk_repr[space_loc][1] = diff
            disk_repr[location][0] = -1
            disk_repr.insert(space_loc, [i, item_len])
    return(disk_repr)

def sum_representation(disk_repr):
    pos = 0
    total = 0
    for chunk in disk_repr:
        if chunk[0] != -1:
            total += sum([i*chunk[0] for i in range(pos, pos + chunk[1])])
        pos += chunk[1]
    return(total)
    
    
with open('Inputs/Input day 9', 'r') as input_file:
    input = [line.rstrip('\n') for line in input_file.readlines()]
    input = ''.join(input)

compressed_file = get_compressed_file(input)
rearranged_chunks = rearrange_chunks(compressed_file)
checksum_2 = sum_representation(rearranged_chunks)

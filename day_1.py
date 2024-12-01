list1 = []
list2 = []

with open("Inputs/Input day 1", "r") as input_file:
    for line in input_file:
        if(len(line) > 1):
            parts = line.split("   ")
            list1.append(int(parts[0]))
            list2.append(int(parts[1].rstrip('\n')))

#Part 1
list1.sort()
list2.sort()
            
diffs = [abs(x - y) for x, y in zip(list1, list2)]
solution = sum(diffs)

#Part 2
similarity = [i * list2.count(i) for i in list1]
solution2 = sum(similarity)
        

    
    


def get_ordering(relations):
    #This assumes that a definitive ordering exists
    lhs = []
    rhs = []    
    for relation in relations:
        lhs.append(relation[0])
        rhs.append(relation[1])

    i = 0
    ordering = {}
    while len(lhs) > 1:
        lowest = set(lhs) - set(rhs)
        if len(lowest) != 1:
            print("No single definitive ordering")
            raise SystemExit
        lowest = list(lowest)[0]
        ordering[lowest] = i
        #Remove matching parts of lists
        for j in reversed(range(0, len(lhs))):
            if lhs[j] == lowest:
                del lhs[j]
                del rhs[j]
        i += 1
        
    if len(set(rhs)) != 1:
        print("No single definitive ordering")
        raise SystemExit
    
    lowest = list(set(lhs))[0]
    highest = list(set(rhs))[0]
    ordering[lowest] = i
    ordering[highest] = i + 1
    
    return(ordering)

def check_book(book):
    ordering = get_ordering([relation for relation in relations if 
                             (relation[0] in book and relation[1] in book)])
    for i in range(0,len(book) - 1):
        if ordering[book[i]] > ordering[book[i+1]]:
            return 0
    return int(book[int((len(book) - 1) / 2)])

#Part 1
with open('Inputs/Input day 5', 'r') as input_file:
    lines = input_file.readlines()

file_divider = lines.index('\n')
lines = [i.rstrip('\n') for i in lines]
relations = [i.split('|') for i in lines[:file_divider]]
books = [i.split(',') for i in lines[file_divider+1:]]

p1_total = sum([check_book(book) for book in books])

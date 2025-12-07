import re

fh = open(r'.\input.txt','r')
lines = [x.strip('\n') for x in fh.readlines()]
fh.close


columns = {}

##Get number of columns and setup columns dict
colFilter = re.compile(r"^\s+1\s+")
colList = filter(colFilter.match, lines).__next__()
colIndex = lines.index(colList)

for i in colList.split():
    columns[i] = []

#print(columns)

##Get columns content ordering
##Stop before line containing column headers


for line in lines[:colIndex]:
    #print(line)
    colCount = 0
    for col in range(0,len(line),4):
        colCount += 1
        colObject = line[col:col+3]
        if colObject.strip():
            columns[str(colCount)].append(re.search(r"\w",colObject).group())

##Reading top down, the stack is backwards. Will need to reverse

part2Columns = {}
for k,v in columns.items():
    columns[k] = v[::-1]
    part2Columns[k] = v[::-1]

#print(columns)


#print(part2Columns)

moveFilter = re.compile(r"^move\s+(\d+)\s+from\s+(\d+)\s+to\s+(\d+)")    
for line in lines[colIndex+2:]:
    moveMatch = moveFilter.match(line)
    moves = moveMatch.groups()
    
    ##Part 1 moves single crate from one stack/column to the next

    for i in range(int(moves[0])):
        columns[moves[-1]].append(columns[moves[1]].pop())
        #print(columns)
    
    ##Part 2 moves the number of crates from stack/column to next in one move
    ##IE: the moved crates stay in the same order

    colHeight = len(part2Columns[moves[1]])
    colMove = part2Columns[moves[1]][colHeight-int(moves[0]):]
    del part2Columns[moves[1]][colHeight-int(moves[0]):]
    part2Columns[moves[-1]].extend(colMove)

part1Answer = []
part2Answer = []
for k,v in columns.items():
    part1Answer.append(v[-1])

for k,v in part2Columns.items():
    part2Answer.append(v[-1])

print("Part 1 answer: ","".join(part1Answer))
print("Part 2 answer: ","".join(part2Answer))




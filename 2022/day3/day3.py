fh = open(r'.\input.txt','r')
lines = [x.strip() for x in fh.readlines()]
fh.close()


#'A' = chr(65)
#'a' = chr(97)
valueDict = {}
partOnePriority = 0
partTwoPriority= 0

for i in range(65,65+26):
    valueDict[chr(i)] = 27 + i - 65

for i in range(97,97+26):
    valueDict[chr(i)] = 1 + i - 97


for line in lines:
    dupList = []
    rucksackLen = len(line)
    compartOne = line[:rucksackLen//2]
    compartTwo = line[rucksackLen//2:]
    for i in compartOne:
        if i in compartTwo:
            if i not in dupList:
                dupList.append(i)
                partOnePriority += valueDict[i]

count = 0
for i in range(0,len(lines),3):
    dupList = []
    for j in lines[i]:
        if j in lines[i+1] and j in lines[i+2] and j not in dupList:
            dupList.append(j)
            partTwoPriority += valueDict[j]
    count += 1

print("Part one answer:",partOnePriority)
print("Part two answer:",partTwoPriority)
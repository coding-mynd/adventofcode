fh = open(r'.\input.txt','r')
lines = [x.strip() for x in fh.readlines()]
fh.close()


print(len(lines))

for line in lines:
    part1Answer = 0
    part2Answer = 0
    for i in range(0,len(line)-1):
        strList = [x for x in line[i:i+4]]
        lineSet = set(strList)
        if len(lineSet) == 4:
            print(lineSet)
            part1Answer = i+4
            break
    
    print("Part One Answer: ",part1Answer)

    for i in range(0,len(line)-1):
        strList = [x for x in line[i:i+14]]
        lineSet = set(strList)
        if len(lineSet) == 14:
            part2Answer = i+14
            break
    
    print("Part Two Answer: ",part2Answer)
    





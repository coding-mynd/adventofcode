fh = open(r'.\input.txt','r')
lines = [x.strip() for x in fh.readlines()]
fh.close()

partOneAnswer = 0
partTwoAnswer = 0

for line in lines:
    pairs = line.split(',')
    section = []
    for pair in pairs:
        for i in pair.split("-"):
            section.append(int(i))
    if (section[0] >= section[2] and section[0] <= section[3] and section[1] >= section[2] and section[1] <= section[3]) or \
       (section[2] >= section[0] and section[2] <= section[1] and section[3] >= section[0] and section[3] <= section[1]):
        partOneAnswer += 1
    
    if (section[0] >= section[2] and section[0] <= section[3]) or \
       (section[1] >= section[2] and section[1] <= section[3]) or \
       (section[2] >= section[0] and section[2] <= section[1]) or \
       (section[3] >= section[0] and section[3] <= section[1]):
        partTwoAnswer += 1

print('Part one answer:',partOneAnswer)
print('Part two answer:',partTwoAnswer)

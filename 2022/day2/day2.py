'''
Advent of Code 2022 Day 2
Rock Paper Scissors Contest
Column 1 is Opponent, Column 2 is you

Part one

A, X = rock = 1 point
B, Y = paper = 2 points
C, Z = scissors = 3 points

Lose = 0 points
Draw = 3 points
Win = 6 points

Example:
A Y = win = 2 + 6 = 8
B X = lose = 1 + 0 = 1
C Z = draw = 3 + 3 = 6

Total = 15

Part two

Column 2 is strategy
X = lose = 0 points
Y = draw = 3 points
Z = win = 6 points

Still need to determine your choice

'''

fh = open(r".\input.txt","r")
lines = [x.strip() for x in fh.readlines()]
fh.close()

#Part 1

partOneTotal = 0
partTwoTotal = 0
pointsDict = {"a":1, "b":2, "c":3}
choiceDict = {"x":"a", "y":"b", "z":"c"}
winsList = ["ab","bc","ca"]
optionsList = ["c","a","b","c","a"]

for line in lines:
    choice = line.lower().split()
    
    #Part 1 totalling
    partOneTotal += pointsDict[choiceDict[choice[1]]]
    if choice[0] == choiceDict[choice[1]]:
        partOneTotal += 3
    elif str(choice[0]+choiceDict[choice[1]]) in winsList:
        partOneTotal += 6

    #Part 2 Totalling
    if choice[1] == "y":
        partTwoTotal += 3 + pointsDict[choice[0]]
    elif choice[1] == "x":
        lostChoice = optionsList[optionsList.index(choice[0],1)-1]
        partTwoTotal += 0 + pointsDict[lostChoice]
    elif choice[1] == "z":
        winChoice = optionsList[optionsList.index(choice[0],1)+1]
        partTwoTotal += 6 + pointsDict[winChoice]

print(f"Day 2 part 1 answer: {partOneTotal}")
print(f"Day 2 part 2 answer: {partTwoTotal}")
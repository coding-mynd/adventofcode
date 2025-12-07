'''
Advent of Code 2015, Day 1
input: file
output: int

Part1: Determine which floor Santa needs to be on
'''

def main():
    path = r"d:\scripts\projects\adventofcode\2015\day1"
    file = r"\input.txt"
    filepath = path + file

    with open(filepath,"r") as fh:
        lines = fh.readlines()

    partone(lines)

def partone(lines):
    floor = 0
    pos = 0
    directions = lines[0]
    for i in range(len(directions)):
        if directions[i] == "(":
            floor += 1
        elif directions[i] == ")":
            floor -= 1
        if floor == -1 and not pos:
            pos = i+1
    
    print(floor,pos)


if __name__ == "__main__":
    main()
'''
Advent of Code 2023, Day 3
input: file
output: int

site: https://adventofcode.com/2023/day/3

Story: engine is broke down, need help finding missing piece
Part 1: Find sum of all numbers adjacent to a symbol; periods "." are not symbols
'''
import re

class part_number():
    def __init__(self,pn,row,col,length):
        self.pn = pn
        self.start = [row, col]
        self.end = [row, col+length-1]
    
    def possible_locations(self):
        self.symbols = []
        #find symbol positiions above and below part_number
        for i in range(self.start[1]-1,self.end[1]+2):
            self.symbols.append([self.start[0]+1,i])
            self.symbols.append([self.start[0]-1,i])
        self.symbols.append([self.start[0],self.start[1]-1])
        self.symbols.append([self.end[0],self.end[1]+1])

    def is_valid(self,grid):
        self.gears = []
        self.valid = False
        grid_start = [0,0]
        grid_end = [len(grid)-1,len(grid[0])-1]
        
        for i in self.symbols:
            if grid_start[0] > i[0] or i[0] > grid_end[0] or \
                grid_end[1] < i[1]  or i[1] < grid_start[1]:
                continue
            location = grid[i[0]][i[1]]
            if location not in [".","\n","\r"] and not location.isnumeric():
                self.valid = True

                #part two asks to find two part numbers adjacent to the same "*" symbol
                if location == "*":
                    self.gears.append(i)



def main():

    parts_list= []
    grid = ["123..2.",
            ".12.12.",
            "..?...."]
    path = r"d:\scripts\projects\adventofcode\2023\day3"
    file = r"\input.txt"
    filepath = path + file

    with open(filepath,"r") as fh:
        grid = fh.readlines()

    find_parts(parts_list,grid)

    partone(parts_list,grid)
    parttwo(parts_list)

def find_parts(parts_list,grid):
    for i in range(len(grid)):
        parts = re.findall(r"\d*",grid[i])
        for p in range(len(parts)):
            if parts[p].isnumeric():
                index = grid[i].index(parts[p])
                #determine if parts_list contains this number in this row
                #if so, find the *last* occurence (ie: greatest col)
                for dup in [x for x in parts_list if x.pn == parts[p] if x.start[0] == i]:
                    print(f"{parts[p]} is a duplicate on line {i}")
                    if dup.start[1] >= index:
                        index = grid[i].find(parts[p],index+1)

                
                #determine if index has part being a sub-string of another part
                #find correct index, if so
                
                for item in parts[:p-1]:
                    if len(parts[p]) == len(item):
                        continue
                    if parts[p] in item:
                        print(f"{parts[p]} is a substring of {item} on line {i}")
                        for parent in [x for x in parts_list if x.start[0] == i if parts[p] in x.pn if x.start[1] <= index if x.end[1] >= index]:
                            index = grid[i].index(parts[p],parent.end[1]+1)
                parts_list.append(part_number(parts[p],i,index,len(parts[p])))


def partone(parts_list,grid):
    sum = 0
    for part in parts_list:
        part.possible_locations()
        part.is_valid(grid)

    valid_parts = [x.pn for x in parts_list if x.valid]

    for i in range(len(valid_parts)):
        sum += int(valid_parts[i])
    print(sum)
    print(len(parts_list),len(valid_parts))
    #print(valid_parts)

def parttwo(parts_list):
    #goal is to find two part numbers sharing the same "*" symbol
    #find the product of these, then add up all gear products

    gear_list = []
    sum = 0
    #find all parts adjacent to a "*" part
    gear_parts = [x for x in parts_list if len(x.gears) > 0]

    for part in gear_parts:
        for gear in part.gears:
            #if parts in gear already found, skip
            if gear in gear_list:
                continue
            #find other parts that same the same gear location
            for item in [x for x in gear_parts if gear in x.gears if x != part]:
                print(part.pn,item.pn,gear)
                sum += int(part.pn) * int(item.pn)
                gear_list.append(gear)
    
    print(sum)
    

if __name__ == "__main__":
    main()


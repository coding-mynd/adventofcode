'''
Advent of Code 2023, Day 10
input: file
output: int

Find the little critter
https://adventofcode.com/2023/day/10

part one: determine pipe path, find furtherest point from starting position
'''
import re,math

class pipe_class():
    connect_dict =  {
        "|" : [[0,1],[0,-1]],
        "-" : [[-1,0],[1,0]],
        "L" : [[0,-1],[1,0]],
        "J" : [[-1,0],[0,-1]],
        "7" : [[-1,0],[0,1]],
        "F" : [[1,0],[0,1]],
        "." : [0,0]
    }

    def __init__(self,pos,type):
        self.pos = pos
        self.type = type
        if type != "S":
            self.adj = self.get_adj()

    def get_adj(self):
        tmp_list = []
        for i in pipe_class.connect_dict[self.type]:
            x_value = self.pos[0] + i[0]
            y_value = self.pos[1] + i[1]
            if x_value < 0 or y_value < 0:
                continue
            tmp_list.append([x_value,y_value])
        return tmp_list
    
    def add_distance(self):
        try:
            self.dist += 1
        except:
            self.dist = 1



def main():

    path = r"d:\scripts\projects\adventofcode\2023\day10"
    file = r"\example1.txt"
    filepath = path + file

    with open(filepath,"r") as fh:
        lines = fh.readlines()
    grid = []

    for i in range(len(lines)):

        for j in range(len(lines[i].strip())):
            grid.append(pipe_class([j,i],lines[i][j]))

    partone(grid)

def partone(grid):

    #find grid member "S" position then all members that connect to it
    #if just two, then we found the adj members

    s_member = [x for x in grid if x.type == "S"][0]
    s_connectors = [x for x in grid if x.type != "S" if s_member.pos in x.adj]
    print(s_member.pos)
    for member in s_connectors:
        member.add_distance()
        print(member.type,member.pos,member.adj,member.dist)
    
    test_case = [x for x in grid if x.pos == [2,0]][0]
    print(test_case.pos,test_case.type,test_case.adj)


if __name__ == "__main__":
    main()



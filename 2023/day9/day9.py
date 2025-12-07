'''
Advnet of Code 2023, Day 9
input: file
output: int

OASIS readings

part one: find number in next sequence for each line; sum up said next seq
part two: find the number before the beginning; sum these
'''
import re

class reading_class():
    def __init__(self,values):
        self.values = [int(x) for x in values]
        self.diff_list = []

    def find_differences(self,values):
        tmp_list = []
        for i in range(len(values)-1):
            tmp_list.append(values[i+1] - values[i])
        self.diff_list.append(tmp_list)
        
        if max(tmp_list) != 0 or min(tmp_list) != 0:
            self.find_differences(tmp_list)
    
    def find_history(self):
        for i in range(len(self.diff_list)-2,-1,-1):
            hist_value = self.diff_list[i][0] - self.diff_list[i+1][0]
            self.diff_list[i].insert(0,hist_value)
        self.values.insert(0,self.values[0]-self.diff_list[0][0])
    
    def __str__(self):
        return str(self.values)


def main():
    path = r"d:\scripts\projects\adventofcode\2023\day9"
    file = r"\input.txt"
    filepath = path + file

    with open(filepath,"r") as fh:
        lines = fh.readlines()

    reading_list = []
    for line in lines:
        reading_list.append(reading_class(line.strip().split()))

    partone(reading_list)
    parttwo(reading_list)

def partone(reading_list):
    line = 1
    for reading in reading_list:
        reading.find_differences(reading.values)
        reading.values.append(sum([x[-1] for x in reading.diff_list]) + reading.values[-1])
        #print(f"{line}:\t",[x[-1] for x in reading.diff_list],reading.values[-1])
        line += 1

    new_total = sum([x.values[-1] for x in reading_list])
    print(f"Total for part one: {new_total}")

def parttwo(reading_list):
    for reading in reading_list:
        reading.find_history()
    
    #print(reading_list[1].diff_list)
    total = sum([x.values[0] for x in reading_list])
    #print([x.values for x in reading_list])

    print(f"Total for part two: {total}")
if __name__ == "__main__":
    main()
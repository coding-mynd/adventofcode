'''
Advent of Code 2023, Day 6
input: file
output: int

input: two lists. First milliseconds a race lasts and second current distance record in millimeters

Boat race. Hold button as soon as race starts. For each millisecond button held, the boat will move that many millimeters per millisecond when let go.


Part 1: Determine count of different hold timers to beat the current record for each race. Mulitply these numbers together
Part 2: Lists of race times and distances are actually just a single race time and distance. Find the number of possible "hold down times" to beat the distance record
'''
import re,math

class race():
    def __init__(self,number,time,record):
        self.number = number
        self.time = int(time)
        self.record = int(record)
    
    def break_record(self):
        breaks = 0
        for i in range(self.time+1):
            distance = i * (self.time - i)
            if distance > self.record:
                breaks += 1
        return breaks

def main():

    path = r"d:\scripts\projects\adventofcode\2023\day6"
    file =r"\input.txt"
    filepath = path + file
    
    with open(filepath,"r") as fh:
        lines = fh.readlines()

    for line in lines:
        if re.search("Time:",line):
            times = re.findall("\d+",line)
        if re.search("Distance:",line):
            records = re.findall("\d+",line)

    
    races = []
    for i in range(len(times)):
        races.append(race(i,times[i],records[i]))

    partone(races)
    parttwo(races)

def partone(races):
    breaking_counts = 1
    for i in races:
        breaking_counts *= i.break_record()
    
    print("Answer to part one:",breaking_counts)

def parttwo(races):
    cat_times = ""
    cat_records = ""
    
    for i in races:
        cat_times += str(i.time)
        cat_records += str(i.record)

    big_race = race(len(races),cat_times,cat_records)

    print("Anser to part two:",big_race.break_record())




if __name__ == "__main__":
    main()
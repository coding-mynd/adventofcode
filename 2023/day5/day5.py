'''
Advent of Code 2023, Day 5
input: file
output: int

Gotta help the gardner on Island Island!
Input is a list of seeds with various number mappings
Mappings are in format: "dst src length"


Part 1: Find the closest location to plant to the first seed
Part 2: Seeds are actually ranges (ie: sendrange1 = [ seeds[0], seeds[0+1] ]). Find closest location
'''
import re,math

class map():
    def __init__(self,name):
        self.name = name
        self.maps = []
    def add_map(self,mapping):
        self.maps.append(mapping)

    def find_dst(self,seed):
        for i in self.maps:
            if i[1] <= seed <= (i[1]+i[2]):
                #print(i)
                return seed -  i[1] + i[0]
        return seed


def main():
    path = r"d:\scripts\projects\adventofcode\2023\day5"
    file = r"\input.txt"
    filepath = path + file
    
    with open(filepath,"r") as fh:
        lines = fh.readlines()

    partone_return = partone(lines)
    print("Answer to Part 1:",partone_return[0])

    parttwo(partone_return)


def partone(lines):
    maps = []
    seeds = []
    seed_maps = {}

    for line in lines:
        if re.search("^seeds:\ ",line): 
            seeds.extend([int(x) for x in re.findall("\d+",line)])
        if re.search("map:",line):
            maps.append(map(re.match("[\w\-]+[\ \t]+",line).group().strip()))
        if re.search("^\d+",line):
            mapping = re.findall("\d+",line)
            int_mapping = [int(i) for i in mapping]
            maps[-1].add_map(int_mapping)
    
    for seed in seeds:
        seed_maps[seed] = [seed]
    #print(maps[0].find_dst(seeds[0]))
    for j in seed_maps:
        #print("seed:",j)
        for i in maps:
            seed_maps[j].append(i.find_dst(seed_maps[j][-1]))
    
    location = seed_maps[seeds[0]][-1]
    for i in seed_maps:
        if location > seed_maps[i][-1]:
            location = seed_maps[i][-1]
    
    return(location,seeds,maps)

def parttwo(array):
    location = array[0]
    seeds = array[1]
    maps = array[2]

    for i in range(len(seeds)-1,0,-2):
        print(seeds[i-1],seeds[i])
        count = 0
        for j in range(seeds[i-1],seeds[i-1]+seeds[i]):
            count += 1
            if not count % 1000000:
                print("negative seed:",i,"seeds left:",seeds[i]-count)
            seed_map = [j]
            for k in maps:
                seed_map.append(k.find_dst(seed_map[-1]))
            if location > seed_map[-1]:
                location = seed_map[-1]
    
    print("Answer to Part two:", location)

if __name__ == "__main__":
    main()

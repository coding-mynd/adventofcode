'''
Advent of Code 2023, Day 8
'''
import re,math

class node():
    def __init__(self,name):
        self.name = name
        self.adj_nodes = {}
    
    def add_node(self,name,dir):
        self.adj_nodes[dir] = name

    def get_adj_node(self,dir):
        return self.adj_nodes[dir]

    def __str__(self):
        return f"{self.name} = ({self.adj_nodes['L']}, {self.adj_nodes['R']})"


def main():
    path = r"d:\scripts\projects\adventofcode\2023\day8"
    file = r"\input.txt"
    filepath = path + file

    with open(filepath,"r") as fh:
        lines = fh.readlines()

    nodelist = []

    for line in lines:
        if re.match(r"^[LR]+\n$",line):
            directions = line.strip()
            continue

        nodes = re.findall(r"\w{3}",line)
        if len(nodes) == 3:
            for n in nodes:
                if len(nodelist) == 0 or n not in [x.name for x in nodelist]:
                    nodelist.append(node(n))
                
            for n in [x for x in nodelist if x.name == nodes[0]]:
                n.add_node(nodes[1],"L")
                n.add_node(nodes[2],"R")

    #partone(nodelist,directions)
    parttwo(nodelist,directions)

def partone(nodes,dir):
    count = 0
    steps = 0
    current_node = [x for x in nodes if x.name == "AAA"][0]
    end_node = [x for x in nodes if x.name == "ZZZ"][0]
    while current_node != end_node:
        if count >= len(dir):
            count = 0
        step = dir[count]
        next_node = current_node.get_adj_node(step)
        current_node = [x for x in nodes if x.name == next_node][0]
        count +=1
        steps += 1

    print(f"Steps to get to {current_node.name} were:",steps)

def parttwo(nodes,dir):
    #first find all nodes that end if A or Z
    current_nodes = [x for x in nodes if x.name[-1] == "A"]
    end_nodes = [x.name for x in nodes if x.name[-1] == "Z"]
    print(end_nodes)
    
    total_steps = 1
    count = 0
    keep_mapping = True
    max_end_nodes = 0
    maps = {}
    while keep_mapping:
        
        if total_steps % 1000000 == 0:
            print(f"nodes left to find path: {len(current_nodes)}",f"total steps: {total_steps}")
        if count >= len(dir):
            count = 0
        step = dir[count]
        next_list = []
        maybe_over = 0
        for n in current_nodes:
            next_list.append(n.get_adj_node(step))
            if next_list[-1] in end_nodes:
                maps[next_list[-1]] = total_steps
                no_output = next_list.pop()

        
        count +=1
        total_steps +=1
        
        if len(next_list) == 0:
            keep_mapping = False
        else:
            current_nodes = []
            for n in next_list:
                current_nodes.append([x for x in nodes if x.name == n][0])
    print(maps)
    sum = 1
    for n in maps.values():
        sum = math.lcm(sum,n)

    
    print(f"Steps to end_nodes is:", sum)




if __name__ == "__main__":
    main()
        
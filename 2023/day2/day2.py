'''
Advent of Code 2023, Day 2
input: file
output: int

site: https://adventofcode.com/2023/day/2

Input is list of game attempts in format:
Game <id>: <int> <color>[, <int> <color>...][; <int> <color>[, <int> <color>]]

where <id> is the game attempt unique id
<int> <color> is number of colors revealed
and reveals are separated by a ";"

Part 1:
    no single reveal can have greater than the below:
        12 red, 13 green, or 14 blue
    sum total of valid game ids

Part 2:
    find the fewest of each color, mulitply together, sum for all games
'''

class game():
    def __init__(self,id):
        self.id = id
        self.reveals = []

    def add_reveal(self,reveal):
        temp_dict = {}
        for i in reveal.split(","):
            i = i.strip()
            j = i.split(" ")
            temp_dict[j[1]] = int(j[0])
        self.reveals.append(temp_dict)

    def __str__(self):
        output = ""
        count = 1
        output += f"id:\t{self.id}\n"
        for i in self.reveals:
            output += f"reveal{count}:\t {str(i)}\n"
            count += 1
        return output

def main():
    path = r"d:\scripts\projects\adventofcode\2023\day2"
    file = "input.txt"
    gamelist = []

    filepath = path + "\\" + file

    with open(filepath,'r') as fh:
        lines = fh.readlines()

    for line in lines:
        line_split = line.split(":")
        game_round = game(line_split[0].split(" ")[-1])
        gamelist.append(game_round)
        for rev in line_split[-1].split(";"):
            game_round.add_reveal(rev)


    partone(gamelist)
    parttwo(gamelist)

def partone(games):
    sum = 0
    for game in games:
        if valid_game(game):
            sum += int(game.id)
    
    print(f"part 1 answer: {sum}")

def parttwo(games):
    sum = 0
    for game in games:
        temp_dict = {}
        for rev in game.reveals:
            for key in rev.keys():
                if temp_dict.__contains__(key):
                    if rev[key] > temp_dict[key]:
                        temp_dict[key] = int(rev[key])
                else:
                    temp_dict[key] = int(rev[key])
        product = 1
        for i in temp_dict.keys():
            product *= temp_dict[i]
        sum += product
    print(f"part 2 anwer: {sum}")

            
            

def valid_game(game):
    max_items = {"red": 12, "green": 13, "blue": 14}
    passed = True

    for reveal in game.reveals:
        for key in reveal.keys():
            if reveal[key] > max_items[key]:
                passed = False
    
    return passed

if __name__ == "__main__":
    main()

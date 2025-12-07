'''
Advent of Code 2023, Day 4
input: file
output: int

Goal is to find winning scratch off (ie: lottery ticket)
Input: game cards separated by line. each card has a list of winning numbers and card numbers separated by a "|"

Part 1: For each winning number found in the card numbers list, the score starts at 1 and is doubled each time
For example, four matches gives the card a value of 8.
Find value for each game card and give the total of all game cards
'''
import re,math

class card():
    def __init__(self,game,win_nums,card_nums):
        self.game = int(game)
        self.win_nums = win_nums
        self.card_nums = card_nums
        self.count = 1
    
    def count_matches(self):
        matches = 0
        for i in self.win_nums:
            if i in self.card_nums:
                matches += 1
        return matches

    def find_next_cards(self,cardList):
        self.next_cards = []
        count = self.count_matches()
        for i in range(1,count+1):
            self.next_cards.extend([x for x in cardList if x.game == self.game + i])
            self.next_cards[-1].count += self.count
        


def main():
    cardList = []
    card_regex = r"^Card\W+(\d+):\W+([\W\d]+)\W+\|\W+([\W\d]+)$"
    
    path = r"d:\scripts\projects\adventofcode\2023\day4"
    file = r"\input.txt"
    filepath = path + file

    with open(filepath,"r") as fh:
        lines = fh.readlines()

    partone(lines,card_regex,cardList)
    parttwo(cardList)

def partone(lines,card_regex,cardList):
    for line in lines:
        card_item = re.search(card_regex,line)
        win_nbrs = re.split("\W+",card_item.group(2))
        card_nbrs = re.split("\W+",card_item.group(3))
        cardList.append(card(card_item.group(1),win_nbrs,card_nbrs))

    sum = 0
    for i in cardList:
        card_points = i.count_matches()
        if card_points:
            sum += math.pow(2,card_points-1)
    print(f"Answer for part 1: {int(sum)}")

def parttwo(cardList):
    sum = 0
    for i in cardList:
        i.find_next_cards(cardList)
        sum += i.count

    print(f"Answer for part 2: {sum}")




if __name__ == "__main__":
    main()
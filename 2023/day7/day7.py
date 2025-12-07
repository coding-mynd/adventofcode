'''
Advent of Code 2023, Day 7
input: file
output: int

input: hands of "Camel Cards" and their bets

Part1: Order hands in descending order of best hand to worst and multiply the bid by the hand placement. Sum all the winnings
Part2: J's are now wild and weakest card. J's give the strongest hand possible

'''
import re,math

class hand_class():

    card_values = {"2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "T":10, "J":11, "Q":12, "K":13, "A":14}
    wild_cards = {"J":2, "2":3, "3":4, "4":5, "5":6, "6":7, "7":8, "8":9, "9":10, "T":11, "Q":12, "K":13, "A":14}

    def __init__(self,cards,bid):
        self.cards = cards
        self.bid = bid
        self.parttwo = False
        self.og_cards = cards
        self.get_cardvalues()

    def set_parttwo(self):
        self.parttwo = True
        self.get_cardvalues()

    def get_cardvalues(self):
        self.card_values = []

        #if parttwo is true, then "J" are the weakest value and use the hand_class.wild_cards values
        if self.parttwo:
            card_values = hand_class.wild_cards
        else:
            card_values = hand_class.card_values
        for card in self.cards:
            self.card_values.append(card_values[card])
    
    def __lt__(self,item):
        #card_values is a list of ints representing the cards
        return self.card_values < item.card_values

    def __str__(self):
        #output giving data on the hand for easy comparison
        str_values = str(self.card_values).replace("[","").replace("]","").replace(" ","")
        return f"{str_values};{self.og_cards};{self.cards};{self.bid}"
    
def main():
    path = r"d:\scripts\projects\adventofcode\2023\day7"
    file = r"\input.txt"
    filepath = path + file

    with open(filepath,"r") as fh:
        lines = fh.readlines()

    hands = []

    #generate a list of hand_class objects
    for line in lines:
        items = line.split()
        hands.append(hand_class(items[0].strip(),int(items[-1].strip())))
        #print(hands[-1])
    

    partone(hands)
    parttwo(hands)

def partone(hands):
    #dict of hand types
    #1 -> 5 of a kind
    #2 -> 4 of a kind
    #3 -> full house
    #4 -> 3 of a kind
    #5 -> two pair
    #6 -> one pair
    #7 -> high card
    winning_hands = {1:[],2:[],3:[],4:[],5:[],6:[],7:[]}
    totalhands = len(hands)

    #sort hands using built-in function againt card_values (list of ints of card_values of the hand)
    #hands are sorted in ascending order and placed in the dict of lists in the same order
    hands.sort()

    sum = 0

    for hand in hands:
        #print(hand)
        #find unique cards in the hand, along with number of unique cards
        unique_cards = set(hand.cards)
        unique_len = len(unique_cards)

        if unique_len == 1:
            #five of a kind
            winning_hands[1].append(hand)
        elif unique_len == 2:
            #full house or four of a kind
            fullhouse = True
            for card in unique_cards:
                #re.findall creates a list of the matching entries
                #if length is 4, then hand must be a four of a kind
                if len(re.findall(card,str(hand.cards))) == 4:
                    fullhouse = False
            if fullhouse:
                winning_hands[3].append(hand)
            else:
                winning_hands[2].append(hand)
        elif unique_len == 3:
            #two pair or three of a kind
            twopair = True
            for card in unique_cards:
                #re.findall creates a list of matching strings
                #if length is 3, hand must a 3 of a kind
                if len(re.findall(card,str(hand.cards))) == 3:
                    twopair = False
            if twopair:
                winning_hands[5].append(hand)
            else:
                winning_hands[4].append(hand)
        elif unique_len == 4:
            #one pair
            winning_hands[6].append(hand)
        elif unique_len == 5:
            #high card
            winning_hands[7].append(hand)
    print("hand_type;card_values;og_cards;current_cards;bid;hand_placement;hand_value")      
    for j in range(1,len(winning_hands)+1):
        #since the sorting put the hands in ascending order
        #need to look at the list is reverse order to get descending order
        for hand in winning_hands[j][::-1]:
            sum += totalhands * hand.bid
            print(f"{j};{hand};{totalhands};{totalhands * hand.bid}")
            totalhands -= 1

    print(sum)

def parttwo(hands):
    '''
    J are now wilds, so give the best hand possible, and worth 1 point
    '''

    for hand in hands:
        hand.set_parttwo()

    for hand in hands:
        #obtain count of wild cards, "J" and unique cards in the hand
        wilds = hand.cards.count("J")
        uniq_cards = set(hand.cards)
        debug = False

        if hand.cards == "J33JJ":
                debug = True


        #If hand is full of wilds, then it's just a 5 of a kind, and doesn't need treated differently
        #idea is to find the wilds and change to the most occuring other card
        #then pass to partone function to sort into the hand types and sum the values
        if wilds:
            if len(uniq_cards) == 1:
                continue

            #add the first card in the unique set to a variable then look for any other
            #unique cards in the set
            #card_list is a list of list of [count,uniq_card]
            #allows for easy sorting to find the uniq_card with the highest count
            card_list = [[1,hand.cards[0]]]
            for card in hand.cards[1:]:
                found = False
                for i in card_list:
                    if card in i:
                        i[0] += 1
                        found = True
                if not found:
                    card_list.append([1,card])
            #card_list is reverse order to have the highest uniq_card count first
            #if highest card is "J", assign next highest to copy_card
            card_list.sort(reverse=True)
            if card_list[0][1] == "J":
                copy_card = card_list[1][1]
            else:
                copy_card = card_list[0][1]
            
            #replace all wilds with highest non-"J" uniq_card
            hand.cards = hand.cards.replace("J",copy_card)
            if hand.og_cards == "J33JJ":
                print(hand.cards)
    
    #call partone to determine hand type
    partone(hands)

if __name__ == "__main__":
    main()
'''
Advent of Code 2023 Day 1
Input: text
Ouput: int

inputs list of strings
finds first and last number for each entry
adds total entries to find sum
outputs said sum
'''
import math

def main():
    file = r".\input.txt"
    with open(file,"r") as fh:
        flist = fh.readlines()

    #part_one(flist)
    part_two(flist)


def part_one(lines):
    int_list = []
    sum = 0
    for i in lines:
        templist = []
        for j in i:
            try:
                templist.append(int(j))
            except:
                pass
        tmp_num = f"{templist[0]}{templist[-1]}"
        int_list.append(int(tmp_num))
        sum += int(tmp_num)

    print(f"part one answer: {sum}")

def part_two(lines):
    dict_list = {
        "1" : 1,
        "one": 1,
        "2" : 2,
        "two" : 2,
        "3" : 3,
        "three" : 3,
        "4" : 4,
        "four" : 4,
        "5" : 5,
        "five" : 5,
        "6" : 6,
        "six" : 6,
        "7" : 7,
        "seven" : 7,
        "8" : 8,
        "eight" : 8,
        "9" : 9,
        "nine" : 9
    }
    sum = 0

    for i in lines:
        i = i.lower()
        temp_dict = {}
        for k,v in dict_list.items():
            try:
                temp_dict[i.index(k)] = v
                temp_dict[i.rindex(k)] = v
            except:
                pass
        key_list = list(temp_dict.keys())
        key_list.sort()
        temp_int = f"{temp_dict[key_list[0]]}" + f"{temp_dict[key_list[-1]]}"
        sum += int(temp_int)
    print(f"part two answer: {sum}")




if __name__ == "__main__":
    main()

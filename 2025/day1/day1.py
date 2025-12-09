
def main():
    '''main function'''

    test = False
    if test:
        file = r'.\input_test.txt'
    else:
        file = r".\input.txt"

    with open(file,"r") as fh:
        lines = fh.readlines()

    clean_lines = [x.strip() for x in lines]

    print(part_one(clean_lines))

def part_one(lines):
    '''runs through the lines'''

    start = 50
    ans = 0
    convert = {"L":-1,"R":1}
    for i in lines:
        add_ans = False
        clicks = int(i[1:])
        ans += int(clicks / 100)
        clicks = convert[i[0]] * (clicks % 100)
        place = start + clicks
        if place > 100:
            place = place - 100
            add_ans = True
        elif place < 0:
            place = place + 100
            add_ans = True
        
        if start != 0 and add_ans:
            ans += 1
        
        if place == 0 or place == 100:
            ans += 1
            place = 0
        #print(start, i, place, ans)
        start = place

    return ans

if __name__ == "__main__":
    main()
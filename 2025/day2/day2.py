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
    func_lines = [x.split(",") for x in clean_lines][0]

    print(part_one(func_lines))
    print(part_two(func_lines))


def part_one(lines):
    '''take range of numbers and find ones with repeating halves'''

    total = 0
    for line in lines:
        ranges = line.split("-")
        for i in range(int(ranges[0]), int(ranges[1])+1):
            num = str(i)
            num_len = len(num)
            if num_len % 2 != 0:
                continue

            if num[:num_len//2] == num[num_len//2:]:
                total += int(num)
    return total

def part_two(lines):
    '''
    find numbers with only sets of repeating characters
    ie: 999, 1010, 121212, 12341234, 823823
    '''
    
    list = []
    for line in lines:
        ranges = line.split("-")
        start = int(ranges[0])
        stop = int(ranges[1])+1

        for i in range(start,stop):
            num = str(i)
            #num = "446446"
            num_len = len(num)
            #print(num)

            if num == num[0]*num_len and num_len > 1:
                #print(num)
                list.append(num)
                continue

            #split in half and compare
            for j in range(num_len // 2,1,-1):
                #print("splitting the number down")
                #only need to find items that might fully repeat
                if num_len % j != 0:
                    continue

                repeats = num_len // j
                repeat_num = num[:j]
                repeat_len = len(repeat_num)
                test_num = num[j:]
                invalid = True
                for k in range(repeats-1):
                    test = test_num[j*k:j*k+repeat_len]
                    #print("num:",num,"repeat_num:",repeat_num,"test:", test)
                    if test != repeat_num:
                        invalid = False
                
                if invalid:
                    #print(num,repeat_num)
                    list.append(num)
                    break

    total = 0
    for i in [int(x) for x in list]:
        total += i

    return total
                
                

            
if __name__ == "__main__":
    main()
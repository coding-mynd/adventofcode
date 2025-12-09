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
    print(part_two(clean_lines))

def part_one(lines):
    '''find the largest two digit number in the line'''
    total = 0
    for line in lines:
        high_index = get_highest_index(line[:len(line)-1])
        sub_str = line[high_index+1:]
        next_index = get_highest_index(sub_str)
        num = line[high_index] + sub_str[next_index]
        total += int(num)
    return total


def part_two(lines):
    '''find large 12 sequence of digits'''
    total = 0
    for line in lines:
        current_index = 0
        numbers = []
        number_length = 12

        for i in range(number_length):
            remaining_numbers = number_length - (len(numbers) + 1)
            search_end_index = len(line) - remaining_numbers
            #print(line,line[current_index:search_end_index])

            max_number = -1
            max_number_index = -1
            for j in range(current_index, search_end_index):
                num = int(line[j])
                #print(num)
                if num > max_number:
                    max_number = num
                    max_number_index = j
            
            numbers.append(str(max_number))
            current_index = max_number_index + 1

        if len(numbers) == number_length:
            joltage = int("".join(numbers))
            #print(joltage)
            total += joltage
    return total



                    


def get_highest_index(num_str):
    for i in range(9,-1,-1):
        find_str = str(i)
        if find_str in num_str:
            return num_str.index(find_str)

if __name__ == "__main__":
    main()
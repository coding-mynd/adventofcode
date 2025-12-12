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
    for i in range(len(lines)):
        if not len(lines[i]):
            ranges_end = i
            ingredients_start = i+1
    range_list = [x.split("-") for x in lines[:ranges_end]]
    ingredient_list = [int(x) for x in lines[ingredients_start:]]

    fresh_count = 0
    for i in ingredient_list:
        fresh = False
        for j in range_list:
           if i >= int(j[0]) and i <= int(j[1]):
            fresh_count += 1
            break

    return fresh_count

def part_two(lines):
    for i in range(len(lines)):
        if not len(lines[i]):
            ranges_end = i

    range_list = [[int(x) for x in lines[0].split("-")]]
    #print(range_list)
    list_of_ranges = [x.split("-") for x in lines[1:ranges_end]]
    #print(list_of_ranges)
    for i in list_of_ranges:
        #print(f"\"{i}\"")
        start_new = []
        end_new = []
        start = int(i[0])
        end = int(i[1])
        #print(start,end)        
        for j in range_list:
            if start >= j[0] and start <= j[1]:
                #if the range is fully within another, it's already counted, so ignore
                if end >= j[0] and end <= j[1]:
                    continue
                start_new.append(j[1]+1)
            elif end >= j[0] and end <= j[1]:
                end_new.append(j[0]-1)
        if len(start_new):
            start = max(start_new)
        if len(end_new):
            end = min(end_new)
        
        range_list.append([start,end])
        #print(range_list)
    
    #print(range_list)
    fresh_total = 0
    for i in range_list:
        fresh_total += i[1] - i[0] + 1

    return fresh_total




if __name__ == "__main__":
    main()
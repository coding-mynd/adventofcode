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
    '''find "@" with less than four others around'''

    #get the dimensions of the grid
    x_max = len(lines[0])
    y_max = len(lines)
    count = 0
    movable = []

    for i in range(y_max):
        for j in range(x_max):
            #need a 3x3 square most times 
            chars = 0
            subarray = []
            if lines[i][j] != "@":
                continue
            if i == 0:
                array1 = lines[i]
                array2 = lines[i+1]
                if j == 0:
                    subarray.append(array1[j:j+2])
                    subarray.append(array2[j:j+2])
                elif j == x_max - 1:
                    subarray.append(array1[j-1:j+1])
                    subarray.append(array2[j-1:j+1])
                else:
                    subarray.append(array1[j-1:j+2])
                    subarray.append(array2[j-1:j+2])
            elif i == y_max - 1:
                array1 = lines[i-1]
                array2 = lines[i]                   
                if j == 0:
                    subarray.append(array1[j:j+2])
                    subarray.append(array2[j:j+2])
                elif j == x_max - 1:
                    subarray.append(array1[j-1:j+1])
                    subarray.append(array2[j-1:j+1])
                else:
                    subarray.append(array1[j-1:j+2])
                    subarray.append(array2[j-1:j+2])
            else:
                array1 = lines[i-1]
                array2 = lines[i]
                array3 = lines[i+1]
                if j == 0:
                    subarray.append(array1[j:j+2])
                    subarray.append(array2[j:j+2])
                    subarray.append(array3[j:j+2])
                elif j == x_max - 1:
                    subarray.append(array1[j-1:j+1])
                    subarray.append(array2[j-1:j+1])
                    subarray.append(array3[j-1:j+1])
                else:
                    subarray.append(array1[j-1:j+2])
                    subarray.append(array2[j-1:j+2])
                    subarray.append(array3[j-1:j+2])
            
            for row in subarray:
                chars += row.count("@")
                #if i == 1 and j == 4:
                #    print(row)

            if chars < 5:
                count += 1
                movable.append([i,j])
    
    #print(movable)
    return count
        
            


def part_two(lines):
    '''find "@" with less than four others around'''

    #get the dimensions of the grid
    x_max = len(lines[0])
    y_max = len(lines)
    count = 0
    anymoves = True

    while anymoves:
        moveable = []
        for i in range(y_max):
            for j in range(x_max):
                chars = 0
                subarray = []
                if lines[i][j] != "@":
                    continue
                if i == 0:
                    array1 = lines[i]
                    array2 = lines[i+1]
                    if j == 0:
                        subarray.append(array1[j:j+2])
                        subarray.append(array2[j:j+2])
                    elif j == x_max - 1:
                        subarray.append(array1[j-1:j+1])
                        subarray.append(array2[j-1:j+1])
                    else:
                        subarray.append(array1[j-1:j+2])
                        subarray.append(array2[j-1:j+2])
                elif i == y_max - 1:
                    array1 = lines[i-1]
                    array2 = lines[i]                   
                    if j == 0:
                        subarray.append(array1[j:j+2])
                        subarray.append(array2[j:j+2])
                    elif j == x_max - 1:
                        subarray.append(array1[j-1:j+1])
                        subarray.append(array2[j-1:j+1])
                    else:
                        subarray.append(array1[j-1:j+2])
                        subarray.append(array2[j-1:j+2])
                else:
                    array1 = lines[i-1]
                    array2 = lines[i]
                    array3 = lines[i+1]
                    if j == 0:
                        subarray.append(array1[j:j+2])
                        subarray.append(array2[j:j+2])
                        subarray.append(array3[j:j+2])
                    elif j == x_max - 1:
                        subarray.append(array1[j-1:j+1])
                        subarray.append(array2[j-1:j+1])
                        subarray.append(array3[j-1:j+1])
                    else:
                        subarray.append(array1[j-1:j+2])
                        subarray.append(array2[j-1:j+2])
                        subarray.append(array3[j-1:j+2])
                
                for row in subarray:
                    chars += row.count("@")
                    #if i == 1 and j == 4:
                    #    print(row)

                if chars < 5:
                    count += 1
                    moveable.append([i,j])
                    tmplist = [x for x in lines[i]]
                    tmplist[j] = "x"
                    lines[i] = "".join(tmplist)
                    

        if len(moveable):
            anymoves = True
            moveable = []
        else:
            anymoves = False

    return count


if __name__ == "__main__":
    main()
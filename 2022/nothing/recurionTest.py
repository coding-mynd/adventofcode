'''
1. Using the head-tail technique, create a recursive concat() function that
is passed an array of strings and returns these strings concatenated
together into a single string. For example, concat(['Hello', 'World'])
should return HelloWorld.

2. Using the head-tail technique, create a recursive product() function that
is passed an array of integers and returns the total multiplied product
of them. This code will be almost identical to the sum() function in this
chapter. However, note that the base case of an array with just one integer
returns the integer, and the base case of an empty array returns 1.

3. Using the flood fill algorithm, count the number of “rooms,” or
enclosed spaces, in a 2D grid. You can do this by creating nested for
loops that call the flood fill function on each character in the grid if
it is a period, in order to change the periods into hash characters. For
example, the following data would result in the program finding six
places in the grid with periods, meaning there are five rooms (and the
space outside all the rooms).
...##########....................................
...#........#....####..................##########
...#........#....#..#...############...#........#
...##########....#..#...#..........#...##.......#
.......#....#....####...#..........#....##......#
.......#....#....#......############.....##.....#
.......######....#........................##....#
.................####........####..........######


'''

import time

def concat(theList):
    if len(theList) == 1:
        return str(theList[0])
    else:
        return str(theList[0]) + concat(theList[1:])

print(concat(['Hello','World',' I','am','a rec','ursion','god-like',' ','entity']))

def product(theList):
    if len(theList) == 0:
        return 1
    elif len(theList) == 1:
        return theList[0]
    else:
        return theList[0] * product(theList[1:])

print(product([3,3,3,3]))


def floodFill(y,x,oldChar,newChar):
    if theGrid[y][x] == oldChar:
        theGrid[y][x] = newChar

        time.sleep(.01)
        for row in theGrid:
            for col in row:
                print(col,end="")
            print("")
        print("\n")

        height = len(theGrid)
        width = len(theGrid[y])
        if x-1 >= 0:
            floodFill(y,x-1,oldChar,newChar)
        if x+1 < width:
            floodFill(y,x+1,oldChar,newChar)
        if y-1 >= 0:
            floodFill(y-1,x,oldChar,newChar)
        if y+1 < height:
            floodFill(y+1,x,oldChar,newChar)

theGrid = [
    list('...##########....................................'),
    list('...#........#....####..................##########'),
    list('...#........#....#..#...############...#........#'),
    list('...##########....#..#...#..........#...##.......#'),
    list('.......#....#....####...#..........#....##......#'),
    list('.......#....#....#......############.....##.....#'),
    list('.......######....#........................##....#'),
    list('.................####........####..........######')
]



for row in theGrid:
    for col in row:
        print(col,end="")
    print("")

floodFill(5,2,"."," ")

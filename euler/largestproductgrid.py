from util import timing
from pkg_resources import resource_filename, resource_listdir
import os

# Project Euler problem 11 solution
# Result: 70600674, pass

def load_data_for_grid():
    global grid
    file = open(resource_filename('resources', 'numbergrid.txt'), 'r')
    lines = filter_lineseparator(file.readlines())
    
    width = len(lines[0].split(','))
    height = len(lines)

    grid = [[0 for x in range(0, width)] for y in range(0, height)]

    for i in range(0, height):
        line = lines[i].split(',')
        for j in range(0, width):
            grid[i][j] = line[j]

    return grid
        

def main():
    load_data_for_grid()
    print("grid loaded")
    right_left_product = 0
    up_down_product = 0
    diag_product = 0

    for i in range(0, len(grid)):
        for j in range(0, len(grid[0])):
            # go right/left
            if j + 3 < len(grid[0]):
                numbers = [grid[i][j], grid[i][j+1], grid[i][j+2], grid[i][j+3]]
                prod = calculate_largest(numbers)

                if right_left_product == 0: right_left_product = prod
                else:
                    if prod > right_left_product: right_left_product = prod
                
            
            # go up/down
            if i + 3 < len(grid):
                numbers = [grid[i][j], grid[i+1][j], grid[i+2][j], grid[i+3][j]]
                prod = calculate_largest(numbers)    

                if up_down_product == 0: up_down_product = prod
                else:
                    if prod > up_down_product: up_down_product = prod

            # go diagonal
            if (i + 3 < len(grid)) and (j + 3 < len(grid[0])):
                numbers = [grid[i][j], grid[i+1][j+1], grid[i+2][j+2], grid[i+3][j+3]]
                prod = calculate_largest(numbers)

                if diag_product == 0: diag_product = prod
                else:
                    if prod > diag_product: diag_product = prod

            if (i - 3 > 0) and (j + 3 < len(grid[0])):
                numbers = [grid[i][j], grid[i-1][j+1], grid[i-2][j+2], grid[i-3][j+3]]
                prod = calculate_largest(numbers)

                if prod > diag_product: diag_product = prod

    print("Left-Right: %d"  % (right_left_product))
    print("Up-Down: %d"  % (up_down_product))
    print("Diagonal: %d"  % (diag_product))

    numbers = [right_left_product, up_down_product, diag_product]
    largest = 0

    for number in numbers:
        if number == 0: largest = number
        else:
            if number > largest: largest = number


    print("Largest: %d" % (largest))



def filter_lineseparator(lines):
    newlines = []
    for line in lines:
        newlines.append(line.replace(os.linesep, ''))

    return newlines


def calculate_largest(numbers):
    product = 1

    for number in numbers:
        product *= int(number)

    return product


if __name__ ==  '__main__':
    main()
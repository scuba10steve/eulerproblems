from util import timing
from pkg_resources import resource_filename, resource_listdir
import os


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
    right_product = 0
    left_product = 0
    up_product = 0
    down_product = 0
    diag_product = 0

    for i in range(0, len(grid)):
        for j in range(0, len(grid[0])):
            # go right/left
            if i + 3 < len(grid):
                numbers = [grid[i][j], grid[i+1][j], grid[i+2][j], grid[i+3][j]]
                prod = calculate_largest(numbers)
                if right_product == 0:
                    right_product = prod
                else:
                    if prod > right_product:
                        right_product = prod
                        




def filter_lineseparator(lines):
    newlines = []
    for line in lines:
        newlines.append(line.replace(os.linesep, ''))

    return newlines


def calculate_largest(numbers):
    product = 1

    for number in numbers:
        product *= number

    return product


if __name__ ==  '__main__':
    main()
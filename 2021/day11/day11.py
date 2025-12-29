import numpy as np

def main():
    
    # Part 1 
    f = open('day11/input.txt', 'r')
    
    matrix = {x+1j*y:int(char) for y, line in enumerate(f.readlines()) for x, char in enumerate(line.strip())}

    steps = 100

    sum1 = 0

    dirs = [1, 1j, -1, -1j, 1+1j, 1-1j, -1+1j, -1-1j]

    def step(pos, flashed):
        matrix[pos] += 1
        if matrix[pos] > 9 and pos not in flashed:
            flashed.add(pos)
            for dir in dirs:
                next = pos + dir
                if next in matrix.keys() and next not in flashed:
                    step(next, flashed)
            
    sum2 = 0

    i = 0

    while True:
        flashed = set()
        for pos, val in matrix.items():
            step(pos, flashed)
        if i < steps:
            sum1 += len(flashed)
        for flash in flashed:
            matrix[flash] = 0
        if len(flashed) == len(matrix):
            sum2 = i + 1
            break
        i += 1

    print('Task 1: ', sum1)
                
    print('Task 2: ', sum2)
    
if __name__ == '__main__':
    main()
import numpy as np

def main():
    
    # Part 1 
    f = open('day07/input.txt', 'r')
    
    positions = f.readline().strip().split(',')
    positions = [int(pos) for pos in positions]

    sums = []
    sums2 = []

    for i in range(min(positions), max(positions)+1):
        this = 0
        this2 = 0
        for pos in positions:
            diff = abs(pos-i)
            this += diff
            for k in range(diff):
                this2 += k+1
        sums.append(this)   
        sums2.append(this2)

    print('Task 1: ', min(sums))
    print('Task 2:', min(sums2))
    
if __name__ == '__main__':
    main()
import numpy as np
from copy import deepcopy

def main():
    
    # Part 1 
    f = open('day06/input.txt', 'r')
    
    fishs = f.readline().strip().split(',')
    fishs = [int(fish) for fish in fishs]

    original_fishs = deepcopy(fishs)

    days = 80

    for i in range(days):
        new = []
        for j in range(len(fishs)):
            if fishs[j] == 0:
                new.append(8)
                fishs[j] = 6
            else:
                fishs[j] -= 1
        fishs.extend(new)

    print('Task 1: ', len(fishs))

    # Part 2

    days2 = 256

    counter =  []
    for i in range(9):
        counter.append(original_fishs.count(i))

    for j in range(days2):

        new_8 = deepcopy(counter[0])
        new_6 = deepcopy(counter[0])

        for k in range(8):
            temp = deepcopy(counter[k+1])
            counter[k] = temp

        counter[6] += new_6
        counter[8] = new_8    

    sum2 = sum(counter)
    
    print('Task 2: ', sum2)

if __name__ == '__main__':
    main()
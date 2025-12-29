import numpy as np
from copy import deepcopy

def main():
    
    # Part 1 
    f = open('day12/input.txt', 'r')
    
    lines = f.readlines()

    path = {}

    for line in lines:
        point1, point2 = line.strip().split('-')

        if point1 not in path:
            path[point1] = [point2]
        else:
            path[point1].append(point2)
        if point2 not in path:
            path[point2] = [point1]
        else:
            path[point2].append(point1)

    paths1 = []
    paths2 = []

    def visited_two_small(curr):
        smalls = [yea for yea in curr if yea.islower()]# and yea != 'end']
        temp = set(smalls)
        if len(temp) != len(smalls):
            return 1
        else:
            return 0

    def step(curr, paths1):
        for val in path[curr[-1]]:
            if val == 'end':
                curr.append(val)
                paths1.append(curr)
            elif val.isupper():
                new = curr + [val]
                step(new, paths1)
            elif val.islower() and val not in curr:
                new = curr + [val]
                step(new, paths1)

    step(['start'], paths1)

    print('Task 1: ', len(paths1))#, paths)

    def step2(curr1, paths2):
        for val in path[curr1[-1]]:
            if val != 'start':
                curr = deepcopy(curr1)
                if val == 'end':
                    curr.append(val)
                    paths2.append(curr)
                elif val.isupper():
                    new = curr + [val]
                    step2(new, paths2)
                elif val.islower(): 
                    if val not in curr:
                        new = curr + [val]
                        step2(new, paths2)
                    elif not visited_two_small(curr):
                        new = curr + [val]
                        step2(new, paths2)

    paths2 = []
    
    step2(['start'], paths2)


    print('Task 2: ', len(paths2))

if __name__ == '__main__':
    main()
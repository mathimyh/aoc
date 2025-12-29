import numpy as np
import math
from re import findall

def main():
    
    # Part 1 
    f = open('day17/test.txt', 'r')
    
    x, y = f.read().strip()[13:].split(',')
    
    x1,x2 = x.split('..')
    y1,y2 = y.split('..')

    x1 = int(x1[3:])
    x2 = int(x2)
    y1 = (int(y1[3:]))
    y2 = (int(y2))

    def run(vx, vy, px=0, py=0):
        if px > x2 or py < y1:
            return 0
        if x2 >= px >= x1 and y1 <= py <= y2:
            return 1
        return run(vx-(vx>0), vy-1, px+vx, py+vy)
    
    bingo = [run(vx, vy) for vx in range(1, x2+1) for vy in range(y1, -y1)]

    print('Task 2: ', sum(bingo))


if __name__ == '__main__':
    main()
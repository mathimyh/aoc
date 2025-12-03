import numpy as np
import sys
import cmath

def main():
    
    # Part 1 
    f = open('day16/test.txt', 'r')
    
    grid = np.array([np.array([(char) for char in line.strip()]) for line in f.readlines()])
    points = ([x + y*1j for x in range(len(grid[0])) for y in range(len(grid))])
    
    sys.setrecursionlimit(1500000) 
    
    for y,row in enumerate(grid):
        for x,col in enumerate(row):
            if col == 'S':
                start = y + x*1j
               
        
    for y,row in enumerate(grid):
        for x,col in enumerate(row):
            if col == 'E':
                end = y + x*1j
    
    paths = []   
    visited = set()    
         
    def search(pos, dir, num):
        # if (pos, dir) in visited:
        #     return
        visited.add((pos, dir))
        # if num >= 12768:
        #     return
        new = pos + dir
        if new in points:
            if grid[int(new.real)][int(new.imag)] == 'E':
                paths.append(num + 1)
            elif grid[int(new.real)][int(new.imag)] != '#':
                grid[int(new.real)][int(new.imag)] = 'B'
                search(new, dir, num+1)
        rotated1 = pos + dir*1j
        if rotated1 in points and (rotated1, dir*1j) not in visited:
            if grid[int(rotated1.real)][int(rotated1.imag)] == 'E':
                paths.append(num + 1001)
            elif grid[int(rotated1.real)][int(rotated1.imag)] != '#':
                grid[int(rotated1.real)][int(rotated1.imag)] = 'R'
                search(rotated1, dir*1j, num+1001)
        rotated2 = pos + dir*-1j
        if rotated2 in points and (rotated2, dir*-1j) not in visited:
            if grid[int(rotated2.real)][int(rotated2.imag)] == 'E':
                paths.append(num + 1001)
            elif grid[int(rotated2.real)][int(rotated2.imag)] != '#':
                grid[int(rotated2.real)][int(rotated2.imag)]  = 'L'
                search(rotated2, dir*-1j, num+1001)  
    
    search(start, 1j, 0)
    
    print(grid)
    
    print('Task 2: ', min(paths))
    
if __name__ == '__main__':
    main()
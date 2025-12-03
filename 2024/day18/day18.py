import numpy as np
import sys

sys.setrecursionlimit(1000000)

def main():
    
    # Part 1 
    f = open('day18/input.txt', 'r')
    
    size = 71
    
    lines = f.readlines()
    
    points = set()
    for i in range(size):
        for j in range(size):
            points.add((i,j))
            
            
    corrupted = set()
    for line in lines[:1024]:
        x,y = line.strip().split(',')
        corrupted.add((int(x), int(y)))
        
    dirs = [(1,0), (0,1), (-1,0), (0,-1)]
    
    visited = set()
    end = (size - 1, size - 1)
    
    ways = []
    
    grid = np.array([np.array(['.' for j in range(size)]) for i in range(size)])
    
    for corrupt in corrupted:
        grid[corrupt[0]][corrupt[1]] = '#'
    
    def search(pos, steps):
        visited.add(pos)
        grid[pos[0]][pos[1]] = str(steps)
        for dir in dirs:
            new = (pos[0] + dir[0], pos[1] + dir[1])
            if new == end:
               ways.append(steps+1)
               print(steps)
            elif new in points and new not in corrupted and new not in visited:
                search(new, steps+1)

    search((0,0), 0)


    np.savetxt('day18/griddy.txt', grid, fmt='%s')
    
    print('Task 1: ', (ways))
    
if __name__ == '__main__':
    main()
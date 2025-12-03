import numpy as np

def main():
    
    # Part 1 
    f = open('day10/test.txt', 'r')
    
    grid = np.array([np.array([int(char) for char in line.strip()]) for line in f.readlines()])
    points = ([(j,i) for i in range(len(grid[0])) for j in range(len(grid))])

    sum_1 = []
    
    def search(coord, done):
        dirs = [(1,0), (0,1), (-1,0), (0,-1)]
        for dir in dirs:
            new = (coord[0] + dir[0], coord[1] + dir[1])
            if new in points:
                if grid[coord[0]][coord[1]] + 1 == grid[new[0]][new[1]]:
                    if grid[new[0]][new[1]] == 9 and (new[0],new[1]) not in done:
                        done.add((new[0],new[1]))
                        sum_1.append(True)
                    else:
                        search(new, done)
                
    indexer = 0    
    for i, x in enumerate(grid):
        for j, y in enumerate(x):
            if y == 0:
                done = set()
                search((i,j), done)
    
    print('Task 1: ', len(sum_1))
    
     # Part 1 
    f = open('day10/input.txt', 'r')
    
    grid = np.array([np.array([int(char) for char in line.strip()]) for line in f.readlines()])
    points = ([(j,i) for i in range(len(grid[0])) for j in range(len(grid))])

    sum_2 = []
    
    def search(coord):
        dirs = [(1,0), (0,1), (-1,0), (0,-1)]
        for dir in dirs:
            new = (coord[0] + dir[0], coord[1] + dir[1])
            if new in points:
                if grid[coord[0]][coord[1]] + 1 == grid[new[0]][new[1]]:
                    if grid[new[0]][new[1]] == 9:
                        sum_2.append(True)
                    else:
                        search(new)
                
    indexer = 0    
    for i, x in enumerate(grid):
        for j, y in enumerate(x):
            if y == 0:
                done = set()
                search((i,j))
    
    print('Task 2: ', len(sum_2))
    
if __name__ == '__main__':
    main()
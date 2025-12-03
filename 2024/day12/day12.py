import numpy as np

def main():
    
    # Part 1 
    f = open('day12/input.txt', 'r')
    
    grid = np.array([np.array([(char) for char in line.strip()]) for line in f.readlines()])
    points = ([(j,i) for i in range(len(grid[0])) for j in range(len(grid))])
    
    neighbors = [(1,0),(0,1),(-1,0),(0,-1)]
    directions = ['right', 'down', 'left', 'up']
    
    sum_1 = 0
    
    regions = []
    done = set()
    
    def search_region(pos, done, region):
        char = grid[pos[0]][pos[1]]
        region.append(pos)
        done.add(pos)
        for neighbor in neighbors:
            next = (pos[0] + neighbor[0], pos[1] + neighbor[1])
            if next in points and grid[next[0]][next[1]] == char and next not in done:
                search_region(next, done, region)
    
    for i, row in enumerate(grid):
        for j, char in enumerate(row):
            region = []
            if (i,j) not in done:
                search_region((i,j), done, region)
            if len(region) > 0:
                regions.append(region)
                
    for region in regions:
        for pos in region:
            tot_nbs = 0
            for neighbor in neighbors:
                next = (pos[0] + neighbor[0], pos[1] + neighbor[1])
                if next in region:
                    tot_nbs += 1
        
              
    # print(regions)        
        
    print('Task 1: ', sum_1)
    
    
    # Task 2 
    
    for region in regions:
        for pos in region:
            tot_nbs = 0
            for neighbor, dir in zip(neighbors, directions):
                next = (pos[0] + neighbor[0], pos[1] + neighbor[1])
                if next not in region:
                    fences[dir].append(next)
    
        
                
    
if __name__ == '__main__':
    main()
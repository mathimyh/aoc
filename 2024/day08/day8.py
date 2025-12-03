import numpy as np

def main():
    
    # Part 1 
    f = open('day8/input.txt', 'r')
    
    grid = np.array([np.array([char for char in line.strip()]) for line in f.readlines()])
    
    antinodes = set()
    
    chars = {}
    
    for i, g in enumerate(grid):
        for j, t in enumerate(g):
            if t != '.':
                if t not in chars.keys():
                    chars[t] = [(i,j)]
                else:
                    chars[t].append((i,j))
                    
    for vals in chars.values():
        for first in vals:
            for second in vals:
                if second != first:
                    antinode = (first[0] + 2*(second[0] - first[0]), first[1] + 2*(second[1] - first[1]))
                    if antinode[0] >= 0 and antinode[0] < len(grid) and antinode[1] >= 0 and antinode[1] < len(grid[0]):
                        antinodes.add(antinode)      
                            
    print('Task 1: ', len(antinodes))


    # Part 2
    
    antinodes2 = set()
    
    for vals in chars.values():
        for first in vals:
            for second in vals:
                if second != first:
                    i = 0
                    antinode = (first[0] + i*(second[0] - first[0]), first[1] + i*(second[1] - first[1]))
                    while antinode[0] >= 0 and antinode[0] < len(grid) and antinode[1] >= 0 and antinode[1] < len(grid[0]):
                        antinodes2.add(antinode)  
                        antinode = (first[0] + i*(second[0] - first[0]), first[1] + i*(second[1] - first[1]))
                        i += 1
                     
    print('Task 2: ', len(antinodes2))
    
if __name__ == '__main__':
    main()
import numpy as np

def main():
    
    # Part 1 
    f = open('2025/day4/input.txt', 'r')
    
    lines = f.readlines()
    
    empty = set()
    rolls = set()
    
    for x, line in enumerate(lines):
        line = line.strip()
        for y, char in enumerate(line):
            pos = x+y*1j
            match char:
                case '@':
                    rolls.add(pos)
                case '.':
                    empty.add(pos)
                
                
    dirs = [x+y*1j for x in range(-1,2) for y in range(-1,2)]
    
    dirs.remove(0+0j) 
       
       
    
    def remove_rolls(rolls):
          
        available = set()
          
        for roll in rolls:
            adjacent = 0
            for dir in dirs:
                if roll + dir in rolls:
                    adjacent += 1
                if adjacent > 3:
                    break
                
            if adjacent < 4:
                available.add(roll)  
                
        return available
        
    available = remove_rolls(rolls)
    
    print('Task 1: ', len(available))
    
    sum2 = len(available)
    
    while len(available) > 0:
        rolls.difference_update(available)
        available = remove_rolls(rolls)
        sum2 += len(available)
        
    print('Task 2: ', sum2)
        
    
if __name__ == '__main__':
    main()
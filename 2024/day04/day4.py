import numpy as np
import sys
from collections import defaultdict

def main():
    
    # Part 1 
    f = open('day4/input.txt', 'r')
    array = np.array([np.array([char for char in line.strip()]) for line in f.readlines()])
    listy = [[char for char in line.strip()] for line in f.readlines()]
    
    
    sum_1 = 0
    
    for line in array:
        string = ''
        for char in line:
            string += char
        sum_1 += string.count('XMAS')
        sum_1 += string[::-1].count('XMAS')
        
    array = np.transpose(array)
    
    for line in array:
        string = ''
        for char in line:
            string += char
        sum_1 += string.count('XMAS')
        sum_1 += string[::-1].count('XMAS')
        
    
    def groups(data, func):
        grouping = defaultdict(list)
        for y in range(len(data)):
            for x in range(len(data[y])):
                grouping[func(x, y)].append(data[y][x])
        return list(map(grouping.get, sorted(grouping)))


    fdiag = groups(array, lambda x, y: x + y)
    bdiag = groups(array, lambda x, y: x - y)
    
    for f in fdiag:
        string = ''
        for char in f:
            string += char
            
        sum_1 += string.count('XMAS')
        sum_1 += string[::-1].count('XMAS')  
      
    for b in bdiag:
        string = ''
        for char in b:
            string += char
        sum_1 += string.count('XMAS')
        sum_1 += string[::-1].count('XMAS')  
          
    
    print('Task 1: ', sum_1)
    
    
    # Task 2 
    
    sum_2 = 0
    
    for x in range(1, len(array)-1):
        for y in range(1, len(array[x])-1):
            if array[x][y] == 'A':
                stars = [array[x+1][y+1], array[x+1][y-1], array[x-1][y+1], array[x-1][y-1]]
                if stars.count('M') == 2 and stars.count('S') == 2 and array[x+1][y+1] != array[x-1][y-1]:
                    sum_2 += 1
           
           
    print('Task 2: ', sum_2)     
    
if __name__ == '__main__':
    main()
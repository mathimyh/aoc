import numpy as np

def main():
    
    # Part 1 
    f = open('2025/day1/input.txt', 'r')
    lines = f.readlines()
    
    
    sum1 = 0
    sum2 = 0
    
    pointing = 50
    
    for line in lines:
        line.strip()
        sign = 1
        
        if line[0] == 'R':
            val = int(line[1:])
        else:
            val = -int(line[1:])
            sign = -1


        for i in range(abs(val)):
            
            pointing += sign
                
            pointing = pointing % 100
            
            if pointing == 0:
                sum2 += 1
            
            
        if pointing == 0:
            sum1 += 1
    
            
    print('Task 1: ', sum1)
    print('Task 2: ', sum2)
    
if __name__ == '__main__':
    main()
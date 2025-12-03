import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import functools

def main():
    
    # Part 1 
    f = open('day11/input.txt', 'r')
    
    stones = f.read().strip().split()
    
    blink = 25
    
    stones0 = []
    
    for i in range(blink):
        new_stones = []
        for j, stone in enumerate(stones):
            if stone == '0':
                new_stones.append('1')
            elif len(stone) % 2 == 0:
                first = str(int(stone[:int(len(stone)*0.5)]))
                second = str(int(stone[int(len(stone)*0.5):]))
                new_stones.append(first)
                new_stones.append(second)
            else:
                new_stones.append(str(int(stone)*2024))
        stones = new_stones
        stones0.append(len(stones))

    print('Task 1: ', len(stones))
    
    
    # Part 2 
    
    f = open('day11/input.txt', 'r').read()
    
    stones = list(map(int, f.split()))
    
    @functools.lru_cache(maxsize=None)
    def one_blink(val):
        
        temp = str(val)
        
        if val == 0:
            return (1, None)
        
        elif len(str(val)) % 2 == 0:
            mid = len(str(val)) // 2
            left = int(temp[:mid])
            right = int(temp[mid:])
            
            return (left, right)
        
        else:
            return (val*2024, None)
        
    @functools.lru_cache(maxsize=None)
    def count_stones(stone, iters):
        
        left, right = one_blink(stone)
        
        if iters == 1:
            if right is None:
                return 1
            else:
                return 2
            
        else:
            
            out = count_stones(left, iters-1)
            if right is not None:
                out += count_stones(right, iters-1)
                
            return out
        
    def run(iters):
        
        sum_2 = 0
        
        for stone in stones:
            sum_2+=count_stones(stone, iters)
            
            
        return sum_2
    
    
    print('Part 2: ', run(75))
    
if __name__ == '__main__':
    main()
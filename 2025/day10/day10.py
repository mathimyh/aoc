import numpy as np
import re
from itertools import combinations
from itertools import combinations_with_replacement
from itertools import chain
from collections import Counter

def main():
    
    # Part 1 
    f = open('2025/day10/input.txt', 'r')
    
    lights = []
    buttons = []
    joltages = []
    
    sum1 = 0
    
    def check_combination(light, buttons):
        result = []
          
        for i in range(len(light)):
            result.append(int(buttons.count(str(i))%2))
    
         
        if result == light:
            return True
        else:
            return False
    
    def check_combination2(joltage, buttons):
        result = []
    
        
        for i in range(len(joltage)):
            result.append(str(buttons.count(str(i))))
         
        # print(result, joltage)
         
        if result == joltage:
            return True
        else:
            return False
    
    lines = f.readlines()
    
    # for line in lines:
        
    #     line = line.strip()
    #     light = re.search(r'([#.]+)', line)
    #     temp = []
    #     for l in light.group():
    #         if l == '#':
    #             temp.append(1)
    #         else:
    #             temp.append(0)
    #     light = temp
    #     # lights.append(light.group() if light else [])
        
    #     rest = re.findall(r'([\d,\s]+)', line)
        
    #     joltage = rest.pop()
    #     joltages.append(joltage)
        
    #     button = [r.split(',') for r in rest if r != ' ']
    #     buttons.append(button)
        
    #     press = 1
    #     while True:
    #         found = False
    #         temp = combinations(button, press)
    #         for t in temp:
    #             tot_button = list(chain(*t))
    #             if check_combination(light, tot_button):
    #                 found = True
    #                 break
    #         if found:
    #             break
    #         else:
    #             press += 1
                
    #     sum1 += press
      
    # print('Task 1: ', sum1)
          
    sum2 = 0 
           
    for line in lines:
        
        line = line.strip()
        light = re.search(r'([#.]+)', line)
        temp = []
        for l in light.group():
            if l == '#':
                temp.append(1)
            else:
                temp.append(0)
        light = temp
        # lights.append(light.group() if light else [])
        
        rest = re.findall(r'([\d,\s]+)', line)
        
        joltage = rest.pop().split(',')
        joltage = [int(j) for j in joltage]
        joltages.append(joltage)
        
        button = [r.split(',') for r in rest if r != ' ']
        buttons.append(button)
        
        press = min(joltage) # Always press more or equal to the least pressed button
        while True:
            found = False
            temp = combinations_with_replacement(button, press)
            
            for t in temp:
                tot_button = Counter(chain.from_iterable(t))
                
                new = [0 for i in range(len(joltage))]
                
                for key, val in tot_button.items():
                    new[int(key)] = val
                    
                if new == joltage:
                    found = True
                    break
                
            if found:
                break
            else:
                press += 1
                
            print(press)
                
        sum2 += press
              
    print('Task 2: ', sum2)    
            

if __name__ == '__main__':
    main()
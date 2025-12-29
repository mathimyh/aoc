import numpy as np
from sympy import Matrix, linsolve
import re
# from itertools import combinations
# from itertools import combinations_with_replacement
# from itertools import chain
# from collections import Count
from scipy.optimize import  linprog
import pulp

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
        
        rest = re.findall(r'([\d,\s]+)', line)
        
        joltage = rest.pop().split(',')
        joltage = [int(j) for j in joltage]
        
        button = [r.split(',') for r in rest if r != ' ']
        
        coefficients = []
        for i in range(len(joltage)):
            temp = [but.count(str(i)) for but in button]
            
            coefficients.append(temp)
            
            
        coefficients1 = np.array(coefficients, dtype=int)
        joltage1 = np.array(joltage, dtype=int)   
        
        lower = [0 for i in range(len(coefficients[0]))]
        upper = [5000 for i in range(len(coefficients[0]))]
        
        n_vars = coefficients1.shape[1]
        
        prob = pulp.LpProblem("MyILP", pulp.LpMinimize)
        
        c = np.ones(n_vars)

        x = [
            pulp.LpVariable(f"x_{i}", lowBound=lower[i], upBound=upper[i], cat="Integer")
            for i in range(n_vars)
        ]
          
        prob += pulp.lpSum(x)
        
        for row_idx in range(coefficients1.shape[0]):
            prob += (
                pulp.lpSum(coefficients1[row_idx, j] * x[j] for j in range(n_vars)) == joltage1[row_idx],
                f"eq_{row_idx}"
            )
            
        prob.solve(pulp.PULP_CBC_CMD(msg=False))
        
        if pulp.LpStatus[prob.status] == "Optimal":
            sol = np.array([v.value() for v in x], dtype=int)
            sum2 += sol.sum()  
              
    print('Task 2: ', sum2)    
            

if __name__ == '__main__':
    main()
    
    
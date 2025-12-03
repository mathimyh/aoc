import numpy as np
import sympy as sym
from sympy.solvers import solve

def main():
    
    # Part 1 
    f = open('day13/input.txt', 'r')
    
    prizes = []
    temp = []
    while True:
        line = f.readline()
        if line == '\n':
            temp = []
        elif line == '':
            break
        else:
            temp.append(line.strip())
            temp.append(f.readline().strip())
            temp.append(f.readline().strip())
    
        if len(prizes) > 0:
            if temp != prizes[-1]:
                prizes.append(temp)
        else:
            prizes.append(temp)
    sum_1 = 0
        
    for prize in prizes:
        
        A_x = int(prize[0].split(':')[1].split(',')[0].split('+')[1])
        A_y = int(prize[0].split(':')[1].split(',')[1].split('+')[1])
        B_x = int(prize[1].split(':')[1].split(',')[0].split('+')[1])
        B_y = int(prize[1].split(':')[1].split(',')[1].split('+')[1])
        P_x = int(prize[2].split(':')[1].split(',')[0].split('=')[1]) + 10000000000000
        P_y = int(prize[2].split(':')[1].split(',')[1].split('=')[1]) + 10000000000000
    
        x,y = sym.symbols('x,y')
        
        eq1 = sym.Eq(A_x*x + B_x*y, P_x)
        eq2 = sym.Eq(A_y*x + B_y*y, P_y)
        
        result = sym.solve([eq1,eq2],(x,y))
        
        
        if result[x].is_integer and result[y].is_integer:
            sum_1 += result[x] * 3 + result[y]
        
    print('Task 1: ', sum_1)
    
if __name__ == '__main__':
    main()
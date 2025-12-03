import numpy as np
import re

def main():
    
    
    f = open('day3/input.txt', 'r')
    data = f.read()
    
    sum_1 = 0
    i = 0
    while True:
        i = data.find('mul(', i+1)
        if i == -1:
            break
        temp = ''
        j = i + 4
        while True:
            if data[j] == ')':
                break
            temp += data[j]
            j += 1
        twos = temp.split(',')
        if len(twos) == 2:
            if twos[0].isdigit() and twos[1].isdigit():
                sum_1 += int(twos[0]) * int(twos[1])
    
    print('Task 1: ', sum_1)
    
    sum_2 = 0
        
    
    i = 0
    do = True
    while True:
        i = re.search("mul\(|do\(\)|don\'t\(\)", str(data))
        if i == None:
            break
        elif i[0] == 'do()':
            do = True
        elif i[0] == 'don\'t()':
            do = False
        elif i[0] == 'mul(' and do:
            temp = ''
            j = i.end()
            while True:
                if data[j] == ')':
                    break
                temp += data[j]
                j += 1
            twos = temp.split(',')
            if len(twos) == 2:
                if twos[0].isdigit() and twos[1].isdigit():
                    sum_2 += int(twos[0]) * int(twos[1])  
        
        data = data[i.end():]
        
       
    
    print('Task 2: ', sum_2)
    
if __name__ == '__main__':
    main() 
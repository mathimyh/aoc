import numpy as np
from copy import deepcopy

def main():
    
    # Part 1 
    f = open('day03/input.txt', 'r')
    
    lines = f.readlines()

    gamma = ''
    epsilon = ''

    for i in range(len(lines[0].strip())):
        ones = 0
        zeros = 0

        for line in lines:
            match line[i]:
                case '1':
                    ones += 1
                case '0':
                    zeros += 1

        if ones > zeros:
            gamma += '1'
            epsilon += '0'
        else:
            gamma += '0'
            epsilon += '1'

    sum1 = int(gamma,2) * int(epsilon,2)

    print('Task 1: ', sum1)

    # Task 2

    def commons(lines):
        
        gamma = ''
        epsilon = ''
        
        for i in range(len(lines[0].strip())):
            ones = 0
            zeros = 0

            for line in lines:
                match line[i]:
                    case '1':
                        ones += 1
                    case '0':
                        zeros += 1

            if ones >= zeros:
                gamma += '1'
                epsilon += '0'
            else:
                gamma += '0'
                epsilon += '1'

        return gamma, epsilon

    oxys = deepcopy(lines)
    co2s = deepcopy(lines)

    for i in range(len(gamma)):
        gamma1, epsilon1 = commons(oxys)
        gamma2, epsilon2 = commons(co2s)
        if len(oxys)>1:
            oxys = [oxy for oxy in oxys if oxy[i] == gamma1[i]]
        if len(co2s)>1:
            co2s = [co2 for co2 in co2s if co2[i] == epsilon2[i]]

    sum2 = int(oxys[0].strip(), 2) * int(co2s[0].strip(), 2) 


    print('Task 2: ', sum2)

    
if __name__ == '__main__':
    main()
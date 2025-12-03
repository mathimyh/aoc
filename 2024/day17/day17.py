import numpy as np
import math


def main():
    
    # Part 1 
    f = open('day17/input.txt', 'r')
    
    A, B, C, trash, progtemp = f.readlines()
    
    A = int(A.strip().split(':')[1])
    B = int(B.strip().split(':')[1])
    C = int(C.strip().split(':')[1])
    
    prog = progtemp.strip().split(':')[1].split(',')
    
    prog = [int(p) for p in prog]
    
    print('Prog: ', prog)
    
    def combo(intg):
        match intg:
            case 0:
                return 0
            case 1:
                return 1
            case 2:
                return 2
            case 3:
                return 3
            case 4:
                return A
            case 5:
                return B
            case 6:
                return C
            case 7:
                print('7 found as combo, what da hell?')
                exit()
    
    outs = []
    
    i = 0
    times = 0
    while i < len(prog):
        match (prog[i]):
            case 0:
                A = math.trunc(A / (2**combo(prog[i+1])))
            case 1:
                B = B ^ prog[i+1]
            case 2:
                B = combo(prog[i+1]) % 8
            case 3:
                if A != 0:
                    i = combo(prog[i+1]) - 2
            case 4: 
                B = B ^ C
            case 5:
                outs.append(combo(prog[i+1]) % 8)
                times += 1
            case 6:
                B = math.trunc(A / (2**combo(prog[i+1])))
            case 7:
                C = math.trunc(A / (2**combo(prog[i+1])))
              
        i += 2
    
    # string = ''
    # for out in outs:
    #     string += str(out)
        
    print('Task 1: ', outs)
    
    
    # Part 2
    
    As = set()
    B = 0
    C = 0
    
    for i in range(1,8):
        pots = [i]
        for j in range(16):
            new = []
            for A in pots:
                for l in range(8):
                    B = A % 8
                    B = B ^ 7
                    C = A >> B
                    B = B ^ 7
                    B = B ^ C
                    if B % 8 == prog[-j-1]:
                        if j != 15:
                            new.append(A*8)
                        else:
                            new.append(A)
                    A += 1
            pots = new
        for A in pots:
            As.add(A)
        
    print('Task 2: ', min(As))
    
if __name__ == '__main__':
    main()
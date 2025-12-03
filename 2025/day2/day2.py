import numpy as np

def main():
    
    # Part 1 
    f = open('2025/day2/input.txt', 'r')
    
    IDs = f.readline().strip().split(',')
    
    sum1 = 0
    sum2 = 0
    
    for ID in IDs:
        
        first, second = ID.split('-')
        
        for val in range(int(first), int(second)+1):
            val = str(val)
            leng = len(val)
            if leng % 2 == 0:
                if val[:int(leng/2)] == val[int(leng/2):]:
                    sum1 += int(val)
                    
            done = False
                    
            for j in range(leng, 1, -1):
                if done:
                    continue
                if leng % j == 0:
                    parts = ([val[k:k + int(leng/j)] for k in range(0, leng-int(leng/j)+1, int(leng/j))])
                    # print(parts)
                    parts = set(parts)
                    if len(parts) == 1:
                        sum2 += int(val)
                        # print(val)
                        done = True

                    
                    
    print('Task 1: ', sum1)
    print('Task 2: ', sum2)
    
    
if __name__ == '__main__':
    main()
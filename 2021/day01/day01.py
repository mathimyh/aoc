import numpy as np

def main():
    
    # Part 1 
    f = open('day01/input.txt', 'r')
    
    l = f.readlines()

    sum = 0

    for i in range(1, len(l)):
        prev = int(l[i-1].strip())
        next = int(l[i].strip())
        # print(prev, next)
        if next > prev:
            sum += 1

    print('Task 1:', sum)
    
    sum2 = 0

    for i in range(2, len(l)-1):
        prev = int(l[i-2].strip()) + int(l[i-1].strip()) + int(l[i].strip())
        next = int(l[i-1].strip()) + int(l[i].strip()) + int(l[i+1].strip())

        if next > prev:
            sum2 += 1

    print('Task 2: ', sum2)
    
if __name__ == '__main__':
    main()
import numpy as np

def main():
    
    # Part 1 
    f = open('day1/input.txt', 'r')
    lines = f.readlines()
    data0 = [line.strip().split('   ')[0] for line in lines]
    data1 = [line.strip().split('   ')[1] for line in lines]
    
    data0 = sorted(data0)
    data1 = sorted(data1)
    
    sum = 0
    for i in range(len(data0)):
        sum += abs(int(data0[i]) - int(data1[i]))
        
    print(sum)
    
    # Part 2 
    
    sum2 = 0
    for elem in data0:
        sum2 += int(elem) * data1.count(elem)
        
    print(sum2)
    
    
if __name__ == '__main__':
    main()
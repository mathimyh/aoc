import numpy as np

def main():
    
    # Part 1 
    f = open('2025/day6/input.txt', 'r')
    
    lines = f.readlines()
    
    operations = lines.pop().strip().split()
    
    sum1 = 0
    
    nums = np.array([np.array([line.strip().split()], int) for line in lines], int)
    
    nums = np.transpose(nums)
    
    for i, row in enumerate(nums):
        
        if operations[i] == '+':
            sum1 += np.sum(row)
        else:
            sum1 +=  np.prod(row)
    
    
    print('Task 1: ', sum1)
    
    sum2 = 0
    
    
    lines = [line[:-1] for line in lines]


    index = 0
    new_nums = []
    
    for j in range(len(lines[0])):
        new_num = ''
        for k in range(4):
            if lines[k][j] != ' ':
                new_num += lines[k][j]
           
        print(new_num)
            
        if new_num != '':
            new_nums.append(int(''.join(new_num)))
        
        else:
            print(new_nums)
            if operations[index] == '+':
                sum2 += np.sum(new_nums)
            else:
                sum2 +=  np.prod(new_nums)
                
            index += 1
            new_nums = []
            
    if operations[index] == '+':
        sum2 += np.sum(new_nums)
    else:
        sum2 +=  np.prod(new_nums)
        
       
    print('Task 2: ', sum2)     
    
if __name__ == '__main__':
    main()
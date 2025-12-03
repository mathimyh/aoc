import numpy as np
import math

def main():
    
    # Part 1 
    f = open('day5/input.txt', 'r')
    
    lines = f.readlines()
    
    commands = {}
    
    sum_1 = 0
    wrong_indexes = []
    for j, line in enumerate(lines):
        if line.strip() == '':
            x = 0
        elif line[2] == '|':
            if not int(line[:2]) in commands.keys():
                commands[int(line[0:2])] = [int(line[3:5])]
            else:
                commands[int(line[0:2])] += [int(line[3:5])]
        else:
            good = True
            nums = line.strip().split(',')
            nums = [int(num) for num in nums]
            for i in range(len(nums)):
                if nums[i] in commands.keys():
                    vals = commands[nums[i]]
                    for val in vals:
                        if val in nums[:i]:
                            good = False
                            wrong_indexes.append([j,nums[i],val])
            if good:
                sum_1 += int(nums[math.trunc(len(nums)/2)])
        
    print('Task 1: ', sum_1)
    
    
    # Part 2 
    
    sum_2 = 0
    
    done = set()
    
    for index, one, two in wrong_indexes:
        
        if index not in done:
        
            nums = lines[index].strip().split(',')
            nums = [int(num) for num in nums]
            
            def swap_and_check(nums, swap_back, swap_forward):
                old1, old2 = nums.index(swap_back), nums.index(swap_forward)
                nums[old1], nums[old2] = nums[old2], nums[old1]
                
                new_swap_back = 0
                new_swap_forward = 0
                
                good = True
                
                for i in range(len(nums)):
                    if nums[i] in commands.keys():
                        vals = commands[nums[i]]
                        for val in vals:
                            if val in nums[:i]:
                                good = False
                                new_swap_back = nums[i]
                                new_swap_forward = val
                
                if not good:
                    swap_and_check(nums, new_swap_back, new_swap_forward)
                    
            swap_and_check(nums, one, two)
                
            sum_2 += int(nums[math.trunc(len(nums)/2)])
        
        done.add(index)
        
    print('Task 2: ', sum_2)
    
if __name__ == '__main__':
    import time
    start = time.time()
    main()
    stop = time.time()
    print(stop-start)
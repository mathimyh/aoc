import numpy as np

def main():
    
    # Part 1 
    f = open('day09/test.txt', 'r')
    
    data = f.read().strip()
    
    
    files = []
    empty = []
    
    sum_1 = 0
    
    for i, char in enumerate(data):
        if i % 2 == 0:
            files.append(int(char))
        else:
            empty.append(int(char))
    
    indexer = 0
    last_indexer = 0
    tot_i = len(files)-1
    new_list = []
    while len(files) > 0:
        
        # The file
        new_list.append((indexer, files[0]))
        files = files[1:]
        
        if len(files) == 0:
            break
        
        # The empty space
        while empty[indexer] > 0:
            if files[-1] > empty[indexer]:
                new_list.append((tot_i - last_indexer, empty[indexer]))
                files[-1] -= empty[indexer]
                empty[indexer] = 0
            elif files[-1] == empty[indexer]:
                new_list.append((tot_i - last_indexer, files[-1]))
                empty[indexer] = 0
                files = files[:-1]
                last_indexer += 1
            else:
                new_list.append((tot_i - last_indexer, files[-1]))
                empty[indexer] -= files[-1]
                files = files[:-1]
                last_indexer += 1
                
        indexer += 1
        
        
    j = 0
    for elem in new_list:
        for k in range(elem[1]):
            sum_1 += j * elem[0]
            j += 1
            
    print('Task 1: ', sum_1)
    
    
    # Part 2
    
    files = []
    empty = []
    
    sum_1 = 0
    
    for i, char in enumerate(data):
        if i % 2 == 0:
            files.append(int(char))
        else:
            empty.append(int(char))
    
    sum_2 = 0
    indexer = 0
    last_indexer = 0
    tot_i = len(files)-1
    new_list_2 = []
    while len(files) > 0:
        # Try moving
        moved = False
        for i in range(len(empty)-indexer):
            if files[-1] <= empty[i]:
                x=0
        
        indexer += 1
        
        
    j = 0
    for elem in new_list_2:
        for k in range(elem[1]):
            sum_2 += j * elem[0]
            j += 1
            
    print(new_list_2)
    print('Task 2: ', sum_2)
    
if __name__ == '__main__':
    main()
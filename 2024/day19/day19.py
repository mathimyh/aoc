import numpy as np

def main():
    
    # Part 1 
    f = open('day19/input.txt', 'r')
    
    avails = f.readline().strip().split(', ')
    
    max_length = 0
    for avail in avails:
        if len(avail) > max_length:
            max_length = len(avail)
    
    trash = f.readline()
    
    towels = f.readlines()
    towels = [towel.strip() for towel in towels]
    
    sum_1 = 0
    
    possibles = set()
    
    # Funker men for tregt.....
    # for i, towel in enumerate(towels):
    #     possible = False
    #     idx = ['']
    #     for j in range(len(towel)):
    #         copy = idx.copy()
    #         idx.clear()
    #         for i in copy:
    #             new = i + towel[j]
    #             if new in avails:
    #                 if j == len(towel) - 1:
    #                     possible = True
    #                     possibles.add(towel)
    #                     break
    #                 else:
    #                     idx.append('')
    #             if j != len(towel) -1:
    #                 if len(new) <= max_length:
    #                     idx.append(new)
            
    #         print(j)
            
    #     if possible:
    #         sum_1 += 1
         
            
    print('Task 1:', sum_1)
    print(possibles)
if __name__ == '__main__':
    main()
import numpy as np
import re

def main():
    
    # Part 1 
    with open('day19\input.txt', 'r', encoding='utf-8') as f:
        text = f.readlines()
    
    array = []
    temp = []
    for line in text[1:]:
        if 'scanner' in line:
            array.append(temp)
            temp = []
            continue
        if line.strip() == '':
            continue
        rows = [int(s) for s in line.strip().split(',')]
        print(rows)
        temp.append(rows)


    print(array)

    
if __name__ == '__main__':
    main()
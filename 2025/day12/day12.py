import numpy as np
import re

def main():
    
    # Part 1 
    f = open('2025/day12/input.txt', 'r')
    
    text = f.read()
    
    actual = [7, 7, 6, 7, 7, 6]
    
    configs = re.findall(r'\d{2}x\d{2}:(?: \d{2})+'  , text)
    
    answer = 0
    
    for config in configs:
        
        size, boxes = config.split(':')
        
        temp = size.split('x')
        
        size = int(temp[0]) * int(temp[1])
        
        box_size = 0
        
        for i, box in enumerate(boxes.split()):
            box_size += actual[i]*int(box)
            
        if box_size < size:
            answer += 1
         
         
    print('Task: ', answer)   
    
if __name__ == '__main__':
    main()
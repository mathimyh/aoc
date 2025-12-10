import numpy as np

def main():
    
    # Part 1 
    f = open('2025/day5/input.txt', 'r')
    
    text = f.read()
    
    ranges, availables = text.split('\n\n')
    
    ranges = ranges.split('\n')
    availables = availables.split('\n')
    
    
    sum1 = 0
    
    for av in availables:
        
        num = int(av)
        
        for range in ranges:
            first, second = range.split('-')
            
            if num >= int(first) and num <= int(second):
                sum1 += 1
                break
        
        
    print('Task 1: ', sum1)
    
    
    range_array = []
    
    for range in ranges:
        f, s = range.split('-')
        range_array.append((int(f), 'f'))
        range_array.append((int(s), 's'))
        
    range_array.sort(key=lambda x: x[0])
    
    starts = 0
    ends = 0
    last = 0
    
    edge_cases = set()
    
    sum2 = 0
    
    for el in range_array:
        if el[1] == 'f':
            if starts == 0:
                last = el[0]
            starts += 1
        else:
            ends += 1
            if starts == ends:
                sum2 += el[0] - last
                if el[0] not in edge_cases and last not in edge_cases:
                    edge_cases.add(el[0])
                    edge_cases.add(last)
                    sum2 += 1
                # elif el[0] in edge_cases and last in edge_cases:
                #     sum2 -= 1
                # print(el[0], last)
                ends = 0
                starts = 0
            
    print('Task 2: ', sum2)
        
if __name__ == '__main__':
    main()
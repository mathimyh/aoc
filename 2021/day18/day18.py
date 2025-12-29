import numpy as np
import ast
import math

def main():
    
    # Part 1 
    f = open('day18/test.txt', 'r')
    

    def map_numbers_with_levels(lst, level=1, result=None):
        if result is None:
            result = []
        if isinstance(lst, int):
            result.append([lst, level])
        elif isinstance(lst, list):
            for item in lst:
                map_numbers_with_levels(item, level+1, result)
        return result

    
    numbers = []

    lines = f.readlines()
    for line in lines:
        s = line.strip()
        numbers.append(s)

    yea = []

    for s in numbers:

        nested_list = ast.literal_eval(s)
        output = map_numbers_with_levels(nested_list, level=0)
        yea.append(output)

    final = yea[0]

    def reduce(listy):
        
        # Explode
        indices = [
        i for i in range(len(listy) - 1)
        if listy[i][1] == 5 and listy[i+1][1] == 5
        ]
        if len(indices) > 0:
            for i in range(0, len(indices), 2):
                idx = indices[i]
                if idx > 0:
                    listy[idx-1][0] += listy[idx][0]
                if idx + 2 < len(listy):
                    listy[idx+2][0] += listy[idx+1][0]
    
            return True
        
        # Split
        for i in range(len(listy)):
            if listy[i][0] >= 10:
                first = math.floor(listy[i][0] / 2)
                second = math.ceil(listy[i][0] / 2)
                level = listy[i][1]
                listy[i] = [first, level + 1]
                listy.insert(i + 1, [second, level + 1])
                return True
            
        return False

    for i in range(1, len(yea)):
        final.extend(yea[i])
        for j in range(len(final)):
            final[j][1] += 1

        while reduce(final):
            pass

    print(final)

    # sum1 = 0

    # for i in range(4, 0, -1):
    #     temp = 0
    #     for i in range(len(final)):
    #         if i < len(final) - 1 and final[i][1] == final[i+1][1] and final[i][1] == i:
    #             temp += 3 * final[i][0] + 2 * final[i+1][0]
    #             break
    #         else:
    #             temp += final[i][0]

    #     sum1 += temp

    # print('Task 1: ', sum1)

if __name__ == '__main__':
    main()
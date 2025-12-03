import numpy as np

def main():
    
    # Part 1 
    f = open('day6/input.txt', 'r')
    
    lines = f.readlines()
    
    matrix = np.array([np.array([char for char in line.strip()]) for line in lines])
    
    current = (None, None)
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == '^':
                current = (i,j)
                
    beginning = current            
    
    dirs = {'^': (-1,0), '>': (0,1), '<': (0,-1), 'v': (1,0)}
    
    been = set()
    
    template_matrix = matrix.copy()
    
    while True:
        
        next = (current[0] + dirs[matrix[current[0]][current[1]]][0], current[1] + dirs[matrix[current[0]][current[1]]][1])
        
        if next[0] >= len(matrix) or next[0] < 0 or next[1] >= len(matrix[0]) or next[1] < 0:
            break
        
        if matrix[next[0]][next[1]] == '#':
            match matrix[current[0]][current[1]]:
                case '^':
                    matrix[current[0]][current[1]] = '>'
                case '<':
                    matrix[current[0]][current[1]] = '^'
                case '>':
                    matrix[current[0]][current[1]] = 'v'
                case 'v':
                    matrix[current[0]][current[1]] = '<'
        else:
            been.add(next)
            matrix[next[0]][next[1]] = matrix[current[0]][current[1]]
            current = next
            
            
    print('Task 1: ', len(been))
    
    # Part 2
    
    sum_2 = 0
    
    current = beginning
    
    for i, j in been:
            
            if (i,j) == beginning or matrix[i][j] == '#':
                x = 0
    
            else:
                
                beens = {'^': set(), '>': set(), '<': set(), 'v': set()}
                matrix = template_matrix.copy()
                current = beginning
                matrix[i][j] = '#'
             
                loop = False    
                
                while True:
                    
                    beens[matrix[current[0]][current[1]]].add((current))
                    
                    next = (current[0] + dirs[matrix[current[0]][current[1]]][0], current[1] + dirs[matrix[current[0]][current[1]]][1])
                                              
                    if next[0] >= len(matrix) or next[0] < 0 or next[1] >= len(matrix[0]) or next[1] < 0:
                        break
                    
                    if next in beens[matrix[current[0]][current[1]]]:
                        loop = True
                        break
                    
                    if matrix[next[0]][next[1]] == '#':
                        match matrix[current[0]][current[1]]:
                            case '^':
                                matrix[current[0]][current[1]] = '>'
                            case '<':
                                matrix[current[0]][current[1]] = '^'
                            case '>':
                                matrix[current[0]][current[1]] = 'v'
                            case 'v':
                                matrix[current[0]][current[1]] = '<'
                    else:
                        matrix[next[0]][next[1]] = matrix[current[0]][current[1]]
                        current = next
                                  
                    
                if loop:
                    sum_2 += 1
    
    print('Task 2: ', sum_2)
    
if __name__ == '__main__':
    main()
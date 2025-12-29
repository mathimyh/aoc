import numpy as np
import matplotlib.pyplot as plt

def main():
    
    # Part 1 
    f = open('day13/input.txt', 'r')
    
    lines = f.readlines()

    matrix = set()

    i = 0
    line = lines[0]
    while line != '\n':

        x, y = line.strip().split(',')

        matrix.add((int(x), int(y)))

        i += 1
        line = lines[i]

    folds = []

    i += 1

    while i < len(lines):

        temp = lines[i].strip().split()[-1]

        dir, pos = temp.split('=')

        folds.append((dir, int(pos)))

        i += 1

    new_matrix = set()

    yea = 1

    for i in range(yea):
        dir = folds[i][0]
        val = folds[i][1]
        for x, y in matrix:
            if dir == 'x':
                if x > val:
                    new = (x - (x - (val))*2, y)
                else:
                    new = (x, y)
            elif dir == 'y':
                if y > val:
                    new = (x, y - (y - (val))*2)
                else:
                    new = (x,y)
            new_matrix.add(new)


    print(len(matrix))
    print('Task 1: ', len(new_matrix))  
    # print(new_matrix) 
    # 

    new_matrix2 = matrix

    for fold in folds: 
        dir = fold[0]
        val = fold[1]
        news = set()
        for x, y in new_matrix2:
            if dir == 'x':
                if x > val:
                    new = (x - (x - (val))*2, y)
                else:
                    new = (x, y)
            elif dir == 'y':
                if y > val:
                    new = (x, y - (y - (val))*2)
                else:
                    new = (x,y)
            news.add(new)
        new_matrix2 = news
    

    # Unzip into x and y lists
    x, y = zip(*new_matrix2)

    plt.scatter(x, y, c='black')
    plt.axis('equal')
    plt.gca().invert_yaxis()  # If you want y=0 at the top like image coordinates
    plt.show()

        
    
if __name__ == '__main__':
    main()
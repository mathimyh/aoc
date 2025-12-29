import numpy as np

def main():
    
    # Part 1 
    f = open('day05/input.txt', 'r')
    
    lines = f.readlines()

    taken = set()
    done = set()

    sum1 = 0

    for line in lines:

        line = line.strip()

        one, two = line.split('->')

        x1, y1 = one.split(',')
        x2, y2 = two.split(',')

        x1 = int(x1)
        y1 = int(y1)
        x2 = int(x2)
        y2 = int(y2)

        if x1 == x2:
            for i in range(min(y1,y2), max(y1,y2)+1):
                if (x1, i) in taken and (x1, i) not in done:
                    sum1 += 1
                    done.add((x1,i))
                else:
                    taken.add((x1, i))

        elif y1 == y2:
            for j in range(min(x1,x2), max(x1,x2)+1):
                if (j, y1) in taken and (j, y1) not in done:
                    sum1 += 1
                    done.add((j,y1))
                else:
                    taken.add((j, y1))

    print('Task 1: ', sum1)

    # Task 2

    taken = set()
    done = set()

    sum2 = 0

    for line in lines:

        line = line.strip()

        one, two = line.split('->')

        x1, y1 = one.split(',')
        x2, y2 = two.split(',')

        x1 = int(x1)
        y1 = int(y1)
        x2 = int(x2)
        y2 = int(y2)

        diff_x = max(x1, x2) - min(x1, x2)
        diff_y = max(y1, y2) - min(y1, y2)  

        if x1 == x2:
            for i in range(min(y1,y2), max(y1,y2)+1):
                if (x1, i) in taken and (x1, i) not in done:
                    sum2 += 1
                    done.add((x1,i))
                else:
                    taken.add((x1, i))

        elif y1 == y2:
            for j in range(min(x1,x2), max(x1,x2)+1):
                if (j, y1) in taken and (j, y1) not in done:
                    sum2 += 1
                    done.add((j,y1))
                else:
                    taken.add((j, y1))

        elif diff_x == diff_y:
            sign = 1 if x2 > x1 else -1
            for k in range(x1, x2+sign, sign):
                sign2 = 1 if y2 > y1 else -1
                for l in range(y1, y2+sign2, sign2):
                    if abs(k - x1) == abs(l - y1):
                        # print((k,l))
                        if (k, l) in taken and (k, l) not in done:
                            sum2 += 1
                            done.add((k,l))
                        else:
                            taken.add((k,l))
                    
    print('Task 2: ', sum2)
    
if __name__ == '__main__':
    main()
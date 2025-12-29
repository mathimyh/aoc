import numpy as np

def main():
    
    # Part 1 
    f = open('day02/input.txt', 'r')
    
    coms = f.readlines()

    depth = 0
    hor = 0

    for com in coms:
        com = com.strip()

        d, val = com.split()

        match d:

            case 'down':
                depth += int(val)
            case 'up':
                depth -= int(val)
            case 'forward':
                hor += int(val)

    sum1 = depth*hor

    print('Task 1: ', sum1)


    # Part 2
    
    depth = 0
    hor = 0
    aim = 0

    for com in coms:
        com = com.strip()

        d, val = com.split()

        match d:

            case 'down':
                aim += int(val)
            case 'up':
                aim -= int(val)
            case 'forward': 
                hor += int(val)
                depth += aim*int(val)

    sum2 = depth*hor

    print('Task 2: ', sum2)
    
if __name__ == '__main__':
    main()
import numpy as np
from copy import deepcopy

def main():
    
    # Part 1 
    f = open('day04/input.txt', 'r')
    
    draws = f.readline()

    draws = draws.strip().split(',')
    draws = [int(draw) for draw in draws]

    boards = []

    rest = f.readlines()

    for i in range(0, len(rest), 6):

        board = []
        
        for j in range(1,6):
            nums = rest[i+j].strip().split()
            temp = []
            for num in nums:
                temp.append(int(num))
            board.append(np.array(temp))

        boards.append(np.array(board))

    # Start drawing numbers

    bingo = 0
    indexer = 5
    drawn= set(draws[:5])

    def check_board(board, drawn)->bool:

        for row in board:
            bingoh = 1
            for num in row:
                if num not in drawn:
                    bingoh = 0
                    break
            if bingoh:
                return 1
        
        return 0

    def sum_board(board, drawn)->int:

        sum = 0

        for row in board:
            for num in row:
                if num not in drawn:
                    sum += int(num)
        return sum
    
    sum1 = 0

    times = 0
    
    while len(boards) > 0 and times < 10000:
        new = (deepcopy(boards))
        bingo = 0
        while not bingo:
            drawn.add(draws[indexer])
            deletes = []
            for i in range(len(boards)):
                if check_board(boards[i], drawn) or check_board(np.transpose(boards[i]), drawn):
                    bingo = 1
                    deletes.append(i)
                    if len(boards) == 1:
                        sum1 = int(draws[indexer])*sum_board(boards[i], drawn)
            new = [arr for i, arr in enumerate(new) if i not in deletes]
            indexer += 1
        

        boards = (new)
        times += 1

        

    print('Task 2: ', sum1)
    
if __name__ == '__main__':
    main()
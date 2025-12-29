import numpy as np

def main():
    
    # Part 1 
    f = open('day10/input.txt', 'r')
    
    lines = f.readlines()

    sum1 = 0

    syntax = {')' : '(', '}' : '{', ']' : '[', '>' : '<'}
    score = {')' : 3, ']' : 57, '}' : 1197, '>' : 25137}
    score2 = {'(' : 1, '[' : 2, '{' : 3, '<' : 4}

    scores = []

    for line in lines:

        ope = []

        corrupted = False
        damn = 0

        for char in line.strip():

            if char in ['(', '[', '{', '<']:
                ope.append(char)
            else:
                if syntax[char] != ope[-1]:
                    sum1 += score[char]
                    corrupted = True
                    break
                else:
                    ope.pop()

        if not corrupted:
            ope.reverse()
            for char in ope:
                damn *= 5
                damn += score2[char]

            scores.append(damn)

    print('Task 1: ', sum1)

    middle = len(scores) // 2 
 
    print('Task 2: ', sorted(scores)[middle])

    
if __name__ == '__main__':
    main()
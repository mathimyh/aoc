import numpy as np
from collections import Counter
from copy import deepcopy
import functools

def main():
    
    # Part 1 
    f = open('day14/input.txt', 'r')
    
    original = f.readline().strip()

    rest = f.readlines()

    rules = {}
    sums = {}

    for line in rest:
        if line != '\n':
            key, val = line.strip().split(' -> ')
            rules[key] = val
            sums[key] = 0
    
    for i in range(len(original)-1):
        curr = original[i] + original[i+1]
        sums[curr] = 1


    steps = 10

    for s in range(steps):

        new = ''

        for i in range(len(original)-1):
            curr = original[i] + original[i+1]
            new += original[i] + rules[curr]
        new += original[-1]

        original = deepcopy(new)

    counts = Counter(original)
    # Find the least and most common
    least_common = min(counts, key=counts.get)
    most_common = max(counts, key=counts.get)
    least_count = counts[least_common]
    most_count = counts[most_common]
    sum1 = most_count - least_count

    print('Task 1: ', sum1)

    # Task 2!

    tpl, _, *rules = open('day14/input.txt').read().split('\n')
    rules = dict(r.split(" -> ") for r in rules)
    pairs = Counter(map(str.__add__, tpl, tpl[1:]))
    chars = Counter(tpl)

    steps2 = 40

    for k in range(steps2):

        for (a,b), c in pairs.copy().items():

            x = rules[a+b]

            pairs[a+b] -= c
            pairs[a+x] += c
            pairs[x+b] += c
            chars[x] += c

    print('Task 2: ', max(chars.values())-min(chars.values()))

if __name__ == '__main__':
    main()
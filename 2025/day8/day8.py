import numpy as np
import heapq

def main():
    
    # Part 1 
    f = open('2025/day8/input.txt', 'r')
    
    boxes = [list(map(int, line.strip().split(','))) for line in f.readlines()]
    
    distances = {} 
    circuits = {}
    
    for i, box in enumerate(boxes):
        
        for j, box2 in enumerate(boxes):
            if j != i:
                distance = abs(np.sqrt((box[0]-box2[0])**2+(box[1]-box2[1])**2+(box[2]-box2[2])**2))
                distances[(min(i,j), max(i,j))] = distance
    
    
    circuits = {}
    which = {}
    counter = 0
    
    sum1 = 0
    pairs = 1000
    
    heap = [(value, key) for key, value in distances.items()]
    heapq.heapify(heap)
    
    sum2 = 0
    
    while True:
        
        dist, next = heapq.heappop(heap)
        
        del distances[next]
        
        # print(which)
        # print(next)
        
        if next[0] not in which.keys() and next[1] not in which.keys():
            circuits[counter] = [next[0], next[1]]
            which[next[0]] = counter
            which[next[1]] = counter
            counter += 1
        
        else:
            if next[0] in which.keys() and next[1] not in which.keys():
                circuits[which[next[0]]].append(next[1])
                which[next[1]] = which[next[0]]
            
            elif next[0] not in which.keys() and next[1] in which.keys():
                # print(which, next)
                circuits[which[next[1]]].append(next[0])
                which[next[0]] = which[next[1]]
            
            elif next[0] in which.keys() and next[1] in which.keys():
                if which[next[0]] != which[next[1]]:
                    circuits[which[next[0]]].extend(circuits[which[next[1]]])
                    # print(next, which[next[0]], which[next[1]])
                    olds = [old for old in circuits[which[next[1]]]]
                    del circuits[which[next[1]]]
                    for old in olds:
                        which[old] = which[next[0]] 
                    # which[next[1]] = which[next[0]]
        # print(next)
        # print(circuits)
        
        if len(circuits) == 1 and len(list(circuits.values())[0]) == len(boxes):
            print(boxes[next[0]], boxes[next[1]])
            print('Task 2: ', int(boxes[next[0]][0]) * int(boxes[next[1]][0]))
            break
    
    # print(which)    
    # print(circuits)
    
    # lengths = [len(val) for k, val in circuits.items()]
    # lengths = sorted(lengths)
    # print(lengths)
    
    # sum1 = lengths[-3] * lengths[-2] * lengths[-1]
    
    
    # print('Task 1: ', sum1)
    # print('Task 2: ', sum2)
    
    
if __name__ == '__main__':
    main()
import numpy as np
import copy
import heapq
from itertools import combinations
from functools import cache

def main():
    
    # Part 1 
    f = open('2025/day11/input.txt', 'r')
    
    lines = [line.strip() for line in f.readlines()]
    
    servers = dict()
    
    for line in lines:
        device, output = line.split(':')
        
        outputs = output.strip().split()
        
        servers[device] = outputs
        
        
    rev_servers = dict()
    
    for key, val in servers.items():
        
        for v in val:
            if v in rev_servers.keys():
                rev_servers[v].append(key)
            else:
                rev_servers[v] = [key]
                      
    
    @cache     
    def cache_step(curr: str, dac: bool, fft: bool) -> int:
        total = 0

        for nxt in servers[curr]:
        
            child_dac = dac
            child_fft = fft

            if nxt == 'dac':
                child_dac = True
            elif nxt == 'fft':
                child_fft = True

            if nxt == 'out':
                if child_dac and child_fft:
                    total += 1
            else:
                total += cache_step(nxt, child_dac, child_fft)
                    
        return total
        
    
    sum = cache_step('svr', False, False)
    
    print(sum) 
    
    
if __name__ == '__main__':
    main()
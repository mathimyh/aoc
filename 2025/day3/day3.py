import numpy as np

def main():
    
    def day3(digits):
    
        sum = 0
    
        f = open('2025/day3/input.txt', 'r')
        
        lines = [line.strip() for line in f.readlines()]
        
        for line in lines:
            
            curr = np.zeros(digits)
            
            for i, char in enumerate(line):
                for j in range(digits):
                    if int(char) > curr[j] and i < len(line)-(digits-1-j):
                        curr[j] = int(char)
                        for k in range(j+1, digits):
                            curr[k] = 0
                        break
            
            sum+= int(''.join(curr.astype(int).astype(str)))
        
        return sum
        
        
    print('Task 1: ', day3(2)) 
    print('Task 2: ', day3(12))
        
    
if __name__ == '__main__':
    main()
import numpy as np

def main():
    
    # Part 2
    f = open('day2/input.txt', 'r')
    lines = f.readlines()
    reports = [line.strip().split() for line in lines]
    # diffs = []
    # for report in reports:
    #     diffs.append(np.array([int(report[i]) - int(report[i-1]) for i in range(1, len(report))]))
        
    sum_safe = 0
    for report in reports:
        dif = np.array([int(report[j]) - int(report[j-1]) for j in range(1, len(report))])
        safe = True
        if not all(dif < 0) and not all(dif > 0): 
            safe = False
        if not all(abs(dif) > 0) or not (all(abs(dif) < 4)):
            safe = False
        if safe:
            sum_safe += 1
        else:
            for i in range(len(report)):
                temp = np.delete(report, i)
                diff = np.array([int(temp[j]) - int(temp[j-1]) for j in range(1, len(temp))])
                safe = True
                if not all(diff < 0) and not all(diff > 0): 
                    safe = False
                if not all(abs(diff) > 0) or not (all(abs(diff) < 4)):
                    safe = False
                if safe:
                    sum_safe += 1
                    break
    
    print('Task 2: ', sum_safe)
        
            
    
if __name__ == '__main__':
    main() 
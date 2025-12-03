def main():
    
    # Part 1 
    f = open('day7/input.txt', 'r')
    lines = f.readlines()
    
    sums = [int(line.strip().split(':')[0]) for line in lines]
    
    terms = [[int(num) for num in line.strip().split(':')[1].split()] for line in lines]
    
    works = [False for i in range(len(sums))]
    
    def multiply_add(terms, index, temp_sum, indox):        
        added = temp_sum + terms[index] 
        multiplied = temp_sum * terms[index]
        concatenated = int(str(temp_sum) + str(terms[index]))
        if index == len(terms)-1:
            if (added == sums[indox] or multiplied == sums[indox] or concatenated == sums[indox]):
                works[indox] = True
        else:
            multiply_add(terms, index+1, added, indox)
            multiply_add(terms, index+1, multiplied, indox)
            multiply_add(terms, index+1, concatenated, indox)
            
    for i in range(len(sums)):
        multiply_add(terms[i], 1, terms[i][0], i)
        
    print('Task 1: ', sum(jodd for jodd, work in zip(sums,works) if work))
            
        
    # Part 2
    
    
        
if __name__ == '__main__':
    main()
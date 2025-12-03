import numpy as np

def main():
    
    # # # Part 1 
    # f = open('day15/input.txt', 'r')
    
    # temp = []
    
    # while True:
    #     newest = f.readline().strip()
    #     if newest != '':
    #         temp.append(newest)
    #     else:
    #         break
            
    # grid = np.array([np.array([char for char in line]) for line in temp])
    # original = grid.copy()
    # current = (0,0)
    # for i in range(len(grid)):
    #     for j in range(len(grid[i])):
    #         if grid[i][j] == '@':
    #             current = (i,j)
    #             break
        
    
    # temp2 = f.read().strip()
    
    # commands = [command.strip() for command in temp2]
    
    # dirs = {'^': (-1,0), 'v': (1,0), '<': (0,-1), '>': (0,1)}
    
    # def move(pos, command):
    #     next = (pos[0] + dirs[command][0], pos[1] + dirs[command][1])
    #     if grid[next[0]][next[1]] == 'O':
    #         move(next, command)
    #     if grid[next[0]][next[1]] == '.':
    #         grid[pos[0]][pos[1]] = '.'
    #         grid[next[0]][next[1]] = 'O'
    
    # for command in commands:
    #     if command != '':
    #         new = (current[0] + dirs[command][0], current[1] + dirs[command][1])
    #         if grid[new[0]][new[1]] == '.':
    #             grid[current[0]][current[1]] = '.'
    #             grid[new[0]][new[1]] = '@'
    #             current = new
    #         elif grid[new[0]][new[1]] == 'O':
    #             move(new, command)
    #             if grid[new[0]][new[1]] == '.':
    #                 grid[current[0]][current[1]] = '.'
    #                 current = new
    #                 grid[new[0]][new[1]] = '@'
       
    # sum_1 = 0   
             
    # for i in range(len(grid)):
    #     for j in range(len(grid[i])):
    #         if grid[i][j] == 'O':
    #             sum_1 += i * 100 + j
                
    # print('Task 1: ', sum_1)
    
    
    # # Task 2
    # grid = []
    # for row in original:
    #     temp = []
    #     for col in row:
    #         if col == '#':
    #             temp.append('#')
    #             temp.append('#')
    #         elif col == '.':
    #             temp.append('.')
    #             temp.append('.')
    #         elif col == 'O':
    #             temp.append('[')
    #             temp.append(']')
    #         else:
    #             temp.append('@')
    #             temp.append('.')
    #     grid.append(np.array(temp))
        
    # grid = np.array(grid)
    
    # def move_vert(pos1, pos2, command, boxes):
    #     boxes.append(pos1)
    #     boxes.append(pos2)
    #     next1 = (pos1[0] + dirs[command][0], pos1[1] + dirs[command][1])
    #     next2 = (pos2[0] + dirs[command][0], pos2[1] + dirs[command][1])
    #     if grid[next1[0]][next1[1]] == '[':
    #         move_vert(next1, next2, command, boxes)
    #     if grid[next1[0]][next1[1]] == ']':
    #         temp = (next1[0], next1[1] - 1)
    #         move_vert(temp, next1, command, boxes)
    #     if grid[next2[0]][next2[1]] == '[':
    #         temp = (next2[0], next2[1] + 1)
    #         move_vert(next2, temp, command, boxes)
    #     # if grid[next2[0]][next2[1]] == ']':
    #     #     move_vert(next1, next2, command, boxes)
        
            
    # def move_hor(pos, command):
    #     next = (pos[0] + dirs[command][0], pos[1] + 2*dirs[command][1])
    #     if grid[next[0]][next[1]] == '[' or grid[next[0]][next[1]] == ']':
    #         move_hor(next, command)
    #     if grid[next[0]][next[1]] == '.':
    #         grid[pos[0]][pos[1]] = '.'
    #         temp = (pos[0], pos[1]+dirs[command][1])
    #         if dirs[command][1] < 0:
    #             grid[temp[0]][temp[1]] = ']'
    #             grid[next[0]][next[1]] = '['
    #         else:
    #             grid[temp[0]][temp[1]] = '['
    #             grid[next[0]][next[1]] = ']'
                
    # def check_and_move_boxes(boxes, command):
    #     for box in boxes:
    #         test = (box[0] + dirs[command][0], box[1] + dirs[command][1])
    #         if grid[test[0]][test[1]] == '#':
    #             return
    #     temps = []
    #     for box in boxes:
    #         temps.append(grid[box[0]][box[1]])
    #         grid[box[0]][box[1]] = '.'
    #     for box, temp in zip(boxes, temps):
    #         new = (box[0] + dirs[command][0], box[1] + dirs[command][1])
    #         grid[new[0]][new[1]] = temp
            
    # current = (0,0)
    # for i in range(len(grid)):
    #     for j in range(len(grid[i])):
    #         if grid[i][j] == '@':
    #             current = (i,j)
    #             break
               
    # for command in commands:
    #     if command != '':
    #         new = (current[0] + dirs[command][0], current[1] + dirs[command][1])
    #         boxes = []
    #         if grid[new[0]][new[1]] == '.':
    #             grid[current[0]][current[1]] = '.'
    #             grid[new[0]][new[1]] = '@'
    #             current = new
    #         elif grid[new[0]][new[1]] == '[':
    #             if command == '>' or command == '<':
    #                 move_hor(new, command)
    #             else:
    #                 move_vert(new, (new[0], new[1]+1), command, boxes)
    #                 check_and_move_boxes(boxes, command)
    #             if grid[new[0]][new[1]] == '.':
    #                 grid[current[0]][current[1]] = '.'
    #                 current = new
    #                 grid[new[0]][new[1]] = '@'
    #         elif grid[new[0]][new[1]] == ']':
    #             if command == '>' or command == '<':
    #                 move_hor(new, command)
    #             else:
    #                 move_vert((new[0], new[1]-1), new, command, boxes)
    #                 check_and_move_boxes(boxes, command)
    #             if grid[new[0]][new[1]] == '.':
    #                 grid[current[0]][current[1]] = '.'
    #                 current = new
    #                 grid[new[0]][new[1]] = '@'

    # sum_2 = 0   
             
    # for i in range(len(grid)):
    #     for j in range(len(grid[i])):
    #         if grid[i][j] == '[':
    #             # if j < len(grid[i]) // 2:
    #             #     print(100*i + j)
    #             sum_2 += 100*i + j
    #             # else:
    #             #     print(100*i + (len(grid[i])-j-2))
    #             #     sum_2 += 100*i + (len(grid[i])-j-2)
                    
                
                
    # np.savetxt('day15/input_grid.txt', grid, fmt='%s')
    
    # print('Task 2: ', sum_2)
        
    grid, moves = open('day15/input.txt').read().split('\n\n')

    def move(p, d):
        p += d
        if all([
            grid[p] != '[' or move(p+1, d) and move(p, d),
            grid[p] != ']' or move(p-1, d) and move(p, d),
            grid[p] != 'O' or move(p, d), grid[p] != '#']):
                grid[p], grid[p-d] = grid[p-d], grid[p]
                return True


    for grid in grid, grid.translate(str.maketrans(
            {'#':'##', '.':'..', 'O':'[]', '@':'@.'})):

        grid = {i+j*1j:c for j,r in enumerate(grid.split())
                        for i,c in enumerate(r)}

        pos, = (p for p in grid if grid[p] == '@')

        for m in moves.replace('\n', ''):
            dir = {'<':-1, '>':+1, '^':-1j, 'v':+1j}[m]
            copy = grid.copy()

            if move(pos, dir): pos += dir
            else: grid = copy

        ans = sum(pos for pos in grid if grid[pos] in 'O[')
        print(int(ans.real + ans.imag*100))
    
    
if __name__ == '__main__':
    main()
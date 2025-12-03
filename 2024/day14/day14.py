import numpy as np
from PIL import Image

def main():
    
    # Part 1 
    f = open('day14/input.txt', 'r')
    
    lines = f.readlines()
    
    width = 101
    height = 103
    
    seconds = 100
    
    sum_1 = 1
    q1 = [(i,j) for i in range(50) for j in range(51)]
    q2 = [(i,j) for i in range(51, 101) for j in range(51)]
    q3 = [(i,j) for i in range(51, 101) for j in range(52, 103)]
    q4 = [(i,j) for i in range(50) for j in range(52, 103)]
    # q1 = [(i,j) for i in range(5) for j in range(3)]
    # q2 = [(i,j) for i in range(6, 11) for j in range(3)]
    # q3 = [(i,j) for i in range(6, 11) for j in range(4, 7)]
    # q4 = [(i,j) for i in range(5) for j in range(4, 7)]
    q1s = 0
    q2s = 0
    q3s = 0
    q4s = 0
    
    grid = np.array([np.array(['.' for j in range(height)]) for i in range(width)])
    
    poses = []
    vels = []
    
    for line in lines:
        pos = (int(line.split()[0].split('=')[1].split(',')[0]), int(line.split()[0].split('=')[1].split(',')[1]))
        vel = (int(line.split()[1].split('=')[1].split(',')[0]), int(line.split()[1].split('=')[1].split(',')[1]))
        poses.append(pos)
        vels.append(vel)  
    
    indexer = 0
    for k in range(500*103*101):
        for i in range(len(poses)):
            new = ((poses[i][0] + vels[i][0])%width, (poses[i][1] + vels[i][1])%height)
            grid[poses[i][0]][poses[i][1]] = '.'
            poses[i] = new
            grid[poses[i][0]][poses[i][1]] = '#'
            
        indexer += 1
        
        # if indexer % 101 == 0 or indexer % 103 == 0:
        image_array = np.where(grid == '#', 255, 0).astype(np.uint8)
        filename = 'day14/yeayey/img_' + str(indexer) + '.png'
        image = Image.fromarray(image_array, mode='L')
        image.save(filename)
            
        
        # if pos in q1:
        #     q1s += 1
        # elif pos in q2:
        #     q2s += 1
        # elif pos in q3:
        #     q3s+=1
        # elif pos in q4:
        #     q4s+=1       
    
    # sum_1 = q1s*q2s*q3s*q4s
    
    # print('Task 1: ', sum_1)
if __name__ == '__main__':
    main()
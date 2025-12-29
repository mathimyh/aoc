import numpy as np

def main():
    
    # Part 1 
    f = open('day09/input.txt', 'r')
    
    lines = f.readlines()

    arr = []

    for line in lines:
        temp = []
        for char in line.strip():
            temp.append(int(char))
        arr.append(np.array(temp))

    arr = np.array(arr)
    
    dirs = [(1,0), (0,1), (-1,0), (0,-1)]

    x_bounds = len(arr)
    y_bounds= len(arr[0])

    sum1 = 0

    points = []

    for x in range(x_bounds):
        for y in range(y_bounds):
            low_point = True
            for dir in dirs:
                if x+dir[0] >= 0 and y+dir[1] >= 0 and x+dir[0] < x_bounds and y+dir[1] < y_bounds:
                    next = arr[x+dir[0]][y+dir[1]]

                    if next <= arr[x][y]:
                        low_point = False
                        break
            if low_point:
                sum1 += 1 + arr[x][y]
                points.append((x,y))
    print('Task 1: ', sum1) 

    basins = []

    taken = set(points)

    def search(curr, basin, taken):
        dirs = [(1,0), (0,1), (-1,0), (0,-1)]
        for dir in dirs:
            next = (curr[0] + dir[0], curr[1]+dir[1])   
            x0, y0 = curr
            x1, y1 = next
            if x1 >= 0 and y1 >= 0 and x1 < x_bounds and y1 < y_bounds:
                if arr[x0][y0] < arr[x1][y1] and arr[x1][y1] != 9 and next not in taken:
                    basin.add(next)
                    taken.add(next)
                    search(next, basin, taken)
                
    basins = [] 

    for point in points:
        basin = set([point])
        search(point, basin, taken)
        basins.append(basin)

    sizes = []
    for basin in basins:
        sizes.append(len(basin))

    top_3 = sorted(sizes, reverse=True)[:3]

    print('Task 2: ', top_3[0]*top_3[1]*top_3[2])

if __name__ == '__main__':
    main()
import numpy as np
from shapely.geometry.polygon import Polygon
from shapely.geometry import box
import matplotlib.pyplot as plt 
from itertools import combinations

def main():
    
    # Part 1 
    f = open('2025/day9/input.txt', 'r')
    
    lines = [line.strip() for line in f.readlines()]
    
    sum1 = 0
    sum2 = 0
    
    border = []
    
    for line in lines:
        x,y = line.split(',')
        border.append((int(x), int(y))) 
    
    rects = [(min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2)) for (x1, y1), (x2, y2) in combinations(border, 2)]
    border = Polygon(border)
    
    areas = [(x2 - x1 + 1) * (y2 - y1 + 1) for (x1, y1, x2, y2) in rects]
    
    sum1 = max(areas)
    
    print('Task 1: ', sum1)
    
    rects = [box(x1,y1,x2,y2) for x1,y1,x2,y2 in rects]
    
    real_rec = 0
    
    for area, rect in zip(areas, rects):
        if border.contains(rect) and area > sum2:
            sum2 = area
            real_rec = rect
    
    def plot_polygon(ax, poly, color, label):
        x, y = poly.exterior.xy
        ax.plot(x, y, color=color, linewidth=2, label=label)
          
    fig, ax = plt.subplots()
    plot_polygon(ax, border, 'red', 'opprinnelig')
    plot_polygon(ax, real_rec, 'blue', 'rect')    
    plt.show()      
                    
    print('Task 2: ', sum2)
       
    
if __name__ == '__main__':
    main()
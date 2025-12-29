import numpy as np
import heapq

def main():
    
    # Part 1 
    f = open('day15/input.txt', 'r')
    matrix = [[int(val) for val in line.strip()] for line in f.readlines()]

    def dijkstra_matrix(grid, start, end):
        rows, cols = len(grid), len(grid[0])
        distances = [[float('inf')] * cols for _ in range(rows)]
        distances[start[0]][start[1]] = 0  # Start cell has cost 0
        heap = [(0, start[0], start[1])]
        directions = [(-1,0), (1,0), (0,-1), (0,1)]  # Up, Down, Left, Right

        while heap:
            cost, r, c = heapq.heappop(heap)

            if (r, c) == end:
                return cost  # Shortest path cost to end

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    new_cost = cost + grid[nr][nc]  # Only add the cost of the next cell
                    if new_cost < distances[nr][nc]:
                        distances[nr][nc] = new_cost
                        heapq.heappush(heap, (new_cost, nr, nc))
        return -1  # If end is unreachable
    start = (0,0)
    end = (len(matrix)-1, len(matrix[0])-1)

    sum1 = dijkstra_matrix(matrix, start, end)

    print('Task 1: ', sum1)

    def expand_matrix(matrix, times=5):
        orig_rows, orig_cols = len(matrix), len(matrix[0])
        new_rows, new_cols = orig_rows * times, orig_cols * times
        expanded = [[0] * new_cols for _ in range(new_rows)]

        for i in range(new_rows):
            for j in range(new_cols):
                
                row_incr = i // orig_rows
                col_incr = j // orig_cols
                incr = row_incr + col_incr
                
                orig_val = matrix[i % orig_rows][j % orig_cols]
                
                new_val = orig_val + incr
                if new_val > 9:
                    new_val = (new_val - 1) % 9 + 1
                expanded[i][j] = new_val

        return expanded

    
    
    expanded_matrix = expand_matrix(matrix, times=5)

    end2 = (len(expanded_matrix)-1, len(expanded_matrix[0])-1)

    sum2 = dijkstra_matrix(expanded_matrix, start, end2)
    
    print('Task 2: ', sum2)

    
    
if __name__ == '__main__':
    main()
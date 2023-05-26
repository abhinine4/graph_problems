
# Q largest island size
import math 

def countislands(grid):
    rows, cols = len(grid), len(grid[0])
    small = math.inf
    seen = set()

    def dfs(grid, r, c, seen):
        if r<0 or c<0 or r==rows or c==cols or (r,c) in seen or grid[r][c] != 'L':
            return 0
        seen.add((r,c))
        size = 1
        size += dfs(grid, r+1, c, seen)
        size += dfs(grid, r-1, c, seen)
        size += dfs(grid, r, c+1, seen)
        size += dfs(grid, r, c-1, seen)

        return size

    for r in range(rows):
        for c in range(cols):
            size = dfs(grid, r, c, seen)
            if size > 0:
                small = min(small, size)
    return small

if __name__== "__main__":
    grid = [
    ['W', 'L', 'W', 'W', 'W'],
    ['W', 'L', 'W', 'W', 'W'],
    ['L', 'L', 'W', 'L', 'W'],
    ['W', 'W', 'L', 'L', 'W'],
    ['L', 'W', 'W', 'L', 'L'],
    ['L', 'L', 'W', 'W', 'W'],
    ]   

    print(countislands(grid))
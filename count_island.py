# count no. of islands in the grid

def countislands(grid):
    rows, cols = len(grid), len(grid[0])
    count = 0
    seen = set()

    def dfs(grid, r, c, seen):
        if r<0 or c<0 or r==rows or c==cols or (r,c) in seen or grid[r][c] != 'L':
            return False
        seen.add((r,c))
        
        dfs(grid, r+1, c, seen)
        dfs(grid, r-1, c, seen)
        dfs(grid, r, c+1, seen)
        dfs(grid, r, c-1, seen)

        return True

    for r in range(rows):
        for c in range(cols):
            if dfs(grid, r, c, seen):
                count += 1 
    return count

if __name__=="__main__":
    grid = [
    ['W', 'L', 'W', 'W', 'L'],
    ['W', 'L', 'W', 'W', 'W'],
    ['L', 'L', 'W', 'L', 'W'],
    ['W', 'W', 'L', 'L', 'W'],
    ['L', 'W', 'W', 'L', 'L'],
    ['L', 'L', 'W', 'W', 'W'],
    ]

    print(countislands(grid))
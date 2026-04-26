def contains_cycle(grid):
    n = len(grid)
    m = len(grid[0])
    
    visited = [[False]*m for _ in range(n)]
    
    def dfs(x, y, px, py, char):
        if visited[x][y]:
            return True
        
        visited[x][y] = True
        
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == char:
                if nx == px and ny == py:
                    continue
                if dfs(nx, ny, x, y, char):
                    return True
        
        return False
    
    for i in range(n):
        for j in range(m):
            if not visited[i][j]:
                if dfs(i, j, -1, -1, grid[i][j]):
                    return True
    
    return False


# -------- USER INPUT --------
n = int(input("Enter number of rows: "))
m = int(input("Enter number of columns: "))

grid = []
print("Enter grid row by row:")
for _ in range(n):
    row = input().split()
    grid.append(row)

# Output
print("Cycle Exists:", contains_cycle(grid))

# Sample Input:
# Enter number of rows: 3
# Enter number of columns: 3
# Enter grid row by row:
# A B C
# D E F
# G H I
# Sample Output:
# Cycle Exists: True
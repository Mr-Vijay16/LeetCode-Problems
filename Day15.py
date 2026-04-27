def hasValidPath(grid):
    n, m = len(grid), len(grid[0])

    # Directions: up, down, left, right
    directions = {
        1: [(0, -1), (0, 1)],      # left, right
        2: [(-1, 0), (1, 0)],      # up, down
        3: [(0, -1), (1, 0)],      # left, down
        4: [(0, 1), (1, 0)],       # right, down
        5: [(0, -1), (-1, 0)],     # left, up
        6: [(0, 1), (-1, 0)]       # right, up
    }

    # Opposite direction mapping
    opposite = {
        (0, -1): (0, 1),
        (0, 1): (0, -1),
        (-1, 0): (1, 0),
        (1, 0): (-1, 0)
    }

    from collections import deque
    queue = deque([(0, 0)])
    visited = set([(0, 0)])

    while queue:
        x, y = queue.popleft()

        if (x, y) == (n - 1, m - 1):
            return True

        for dx, dy in directions[grid[x][y]]:
            nx, ny = x + dx, y + dy

            if 0 <= nx < n and 0 <= ny < m:
                # Check if next cell connects back
                if opposite[(dx, dy)] in directions[grid[nx][ny]]:
                    if (nx, ny) not in visited:
                        visited.add((nx, ny))
                        queue.append((nx, ny))

    return False


# -------- USER INPUT --------
n = int(input("Enter number of rows: "))
m = int(input("Enter number of columns: "))

grid = []
print("Enter grid values:")
for _ in range(n):
    row = list(map(int, input().split()))
    grid.append(row)

# Output
print("Valid Path Exists:", hasValidPath(grid))

#sample input:
# Enter number of rows: 3
# Enter number of columns: 3
# Enter grid values:
# 1 2 3
# 4 5 6
# 7 8 9
# Valid Path Exists: True
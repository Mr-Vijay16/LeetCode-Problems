def rotateGrid(grid, k):
    m = len(grid)
    n = len(grid[0])

    layers = min(m, n) // 2

    for layer in range(layers):

        elements = []

        # Top row
        for j in range(layer, n - layer):
            elements.append(grid[layer][j])

        # Right column
        for i in range(layer + 1, m - layer - 1):
            elements.append(grid[i][n - layer - 1])

        # Bottom row
        for j in range(n - layer - 1, layer - 1, -1):
            elements.append(grid[m - layer - 1][j])

        # Left column
        for i in range(m - layer - 2, layer, -1):
            elements.append(grid[i][layer])

        # Rotate counter-clockwise
        size = len(elements)
        k_mod = k % size
        rotated = elements[k_mod:] + elements[:k_mod]

        idx = 0

        #Fill Top row
        for j in range(layer, n - layer):
            grid[layer][j] = rotated[idx]
            idx += 1

        #Right column
        for i in range(layer + 1, m - layer - 1):
            grid[i][n - layer - 1] = rotated[idx]
            idx += 1

        #Bottom row
        for j in range(n - layer - 1, layer - 1, -1):
            grid[m - layer - 1][j] = rotated[idx]
            idx += 1

        #Left column
        for i in range(m - layer - 2, layer, -1):
            grid[i][layer] = rotated[idx]
            idx += 1

    return grid




m = int(input("Enter number of rows: "))
n = int(input("Enter number of columns: "))

print("Enter matrix rows:")

grid = []
for _ in range(m):
    row = list(map(int, input().split()))
    grid.append(row)

k = int(input("Enter number of rotations: "))


result = rotateGrid(grid, k)


print("Rotated Grid:")

for row in result:
    print(row)
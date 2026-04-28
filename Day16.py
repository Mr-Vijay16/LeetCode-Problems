def minOperations(grid, x):
    # Flatten the grid
    arr = []
    for row in grid:
        for val in row:
            arr.append(val)

    # Check feasibility (all elements must have same remainder mod x)
    remainder = arr[0] % x
    for num in arr:
        if num % x != remainder:
            return -1

    # Sort array
    arr.sort()

    # Median gives minimum operations
    median = arr[len(arr) // 2]

    # Calculate operations
    operations = 0
    for num in arr:
        operations += abs(num - median) // x

    return operations


# -------- USER INPUT --------
n = int(input("Enter number of rows: "))
m = int(input("Enter number of columns: "))

print("Enter grid values:")
grid = []
for _ in range(n):
    row = list(map(int, input().split()))
    grid.append(row)

x = int(input("Enter value of x: "))

# Output
result = minOperations(grid, x)
print("Minimum Operations:", result)
#sample input:
# Enter number of rows: 3
# Enter number of columns: 3
# Enter grid values:
# 1 2 3
# 4 5 6
# 7 8 9
# Enter value of x: 2
# Minimum Operations: 3
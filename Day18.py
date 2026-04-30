def maxPathScore(grid, k):
    n = len(grid)
    m = len(grid[0])

    # dp[i][j][c] = max score reaching (i,j) with cost c
    dp = [[[-1]*(k+1) for _ in range(m)] for _ in range(n)]

    # Initial cell
    start_cost = 0 if grid[0][0] == 0 else 1
    if start_cost <= k:
        dp[0][0][start_cost] = grid[0][0]

    for i in range(n):
        for j in range(m):
            for c in range(k+1):
                if dp[i][j][c] == -1:
                    continue

                # Move Right
                if j + 1 < m:
                    new_cost = c + (0 if grid[i][j+1] == 0 else 1)
                    if new_cost <= k:
                        dp[i][j+1][new_cost] = max(
                            dp[i][j+1][new_cost],
                            dp[i][j][c] + grid[i][j+1]
                        )

                # Move Down
                if i + 1 < n:
                    new_cost = c + (0 if grid[i+1][j] == 0 else 1)
                    if new_cost <= k:
                        dp[i+1][j][new_cost] = max(
                            dp[i+1][j][new_cost],
                            dp[i][j][c] + grid[i+1][j]
                        )

    # Find best score at destination
    ans = max(dp[n-1][m-1])
    return ans if ans != -1 else -1


# -------- USER INPUT --------
n = int(input("Enter number of rows: "))
m = int(input("Enter number of columns: "))

print("Enter grid values (0,1,2):")
grid = []
for _ in range(n):
    row = list(map(int, input().split()))
    grid.append(row)

k = int(input("Enter maximum cost k: "))

# Output
print("Maximum Path Score:", maxPathScore(grid, k))

#sample output
#Enter number of columns: 2
#Enter grid values:
#0 1
#2 0
#Enter maximum cost k: 1

#Maximum Path Score: 2
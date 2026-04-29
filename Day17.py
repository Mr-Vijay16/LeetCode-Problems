def maxScore(grid):
    n = len(grid)

    # Prefix sum for each column
    prefix = [[0]*n for _ in range(n)]
    for j in range(n):
        prefix[0][j] = grid[0][j]
        for i in range(1, n):
            prefix[i][j] = prefix[i-1][j] + grid[i][j]

    # DP[col][height]
    dp = [[0]*(n+1) for _ in range(n+1)]

    for col in range(n-1, -1, -1):
        for h in range(n+1):
            best = 0

            for nh in range(n+1):
                score = dp[col+1][nh]

                # Add contribution
                if nh > h:
                    score += prefix[nh-1][col]
                elif nh < h:
                    score += prefix[h-1][col]

                best = max(best, score)

            dp[col][h] = best

    return dp[0][0]


# -------- USER INPUT --------
n = int(input("Enter grid size (n x n): "))

print("Enter grid values:")
grid = []
for _ in range(n):
    row = list(map(int, input().split()))
    grid.append(row)

# Output
print("Maximum Score:", maxScore(grid))

# Sample Input:
# Enter grid size (n x n): 3
# Enter grid values:
# 1 2 3
# 4 5 6
# 7 8 9
# Maximum Score: 49
# Take input
colors = list(map(int, input("Enter house colors (space separated): ").split()))

n = len(colors)
max_dist = 0

# Compare from both ends
for i in range(n):
    if colors[i] != colors[0]:
        max_dist = max(max_dist, i)
    if colors[i] != colors[-1]:
        max_dist = max(max_dist, n - 1 - i)

# Output
print("Maximum Distance:", max_dist)

#output
# Enter house colors (space separated): 1 1 1 6 1
# Maximum Distance: 3
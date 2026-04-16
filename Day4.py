# Take input
nums = list(map(int, input("Enter array elements (space separated): ").split()))
queries = list(map(int, input("Enter query indices (space separated): ").split()))

from collections import defaultdict
import bisect

n = len(nums)

# Store indices of each value
pos = defaultdict(list)
for i in range(n):
    pos[nums[i]].append(i)

result = []

# Process each query
for q in queries:
    value = nums[q]
    indices = pos[value]

    # If only one occurrence
    if len(indices) == 1:
        result.append(-1)
        continue

    # Binary search position
    i = bisect.bisect_left(indices, q)

    # Left neighbor
    left = indices[i - 1] if i > 0 else indices[-1]

    # Right neighbor
    right = indices[i + 1] if i < len(indices) - 1 else indices[0]

    # Circular distance
    dist_left = abs(q - left)
    dist_right = abs(q - right)

    dist_left = min(dist_left, n - dist_left)
    dist_right = min(dist_right, n - dist_right)

    result.append(min(dist_left, dist_right))

# Output result
print("Output:", result)

#output:
#Enter array elements (space separated): 1 3 1 4 1 3 2
#Enter query indices (space separated): 0 3 5
#Output: [2, -1, 3]

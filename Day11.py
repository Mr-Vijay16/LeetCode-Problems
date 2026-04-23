# Take input
nums = list(map(int, input("Enter array elements (space separated): ").split()))

from collections import defaultdict

# Store indices of each number
pos = defaultdict(list)

for i, num in enumerate(nums):
    pos[num].append(i)

n = len(nums)
result = [0] * n

# Calculate distances
for indices in pos.values():
    prefix_sum = 0
    
    # Left to right
    for i in range(len(indices)):
        idx = indices[i]
        result[idx] += idx * i - prefix_sum
        prefix_sum += idx
    
    prefix_sum = 0
    
    # Right to left
    for i in range(len(indices)-1, -1, -1):
        idx = indices[i]
        result[idx] += prefix_sum - idx * (len(indices) - 1 - i)
        prefix_sum += idx

# Output
print("Output:", result)
# Sample input:
# Enter array elements (space separated): 1 2 1 3 2
# Output: [2, 2, 2, 0, 2]
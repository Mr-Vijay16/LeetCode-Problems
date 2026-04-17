# Function to reverse a number
def reverse_num(x):
    return int(str(x)[::-1])

# Take input
nums = list(map(int, input("Enter numbers (space separated): ").split()))

seen = {}
min_dist = float('inf')

# Loop through array
for i, num in enumerate(nums):
    
    # Check if current number matches any stored reverse
    if num in seen:
        min_dist = min(min_dist, i - seen[num])
    
    # Store reverse of current number
    rev = reverse_num(num)
    seen[rev] = i

# Output result
if min_dist == float('inf'):
    print(-1)
else:
    print("Minimum Distance:", min_dist)

#output:
#Enter numbers (space separated): 120 21
#Minimum Distance: 1
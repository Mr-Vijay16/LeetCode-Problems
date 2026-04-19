# Take input
nums1 = list(map(int, input("Enter nums1 (space separated): ").split()))
nums2 = list(map(int, input("Enter nums2 (space separated): ").split()))

i = 0
j = 0
max_dist = 0

# Two pointer approach
while i < len(nums1) and j < len(nums2):
    if nums1[i] <= nums2[j]:
        max_dist = max(max_dist, j - i)
        j += 1
    else:
        i += 1

# Output
print("Maximum Distance:", max_dist)
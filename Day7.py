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


print("Maximum Distance:", max_dist)

#Sample Input
#Enter nums1 (space separated): 55 30 5 4 2
#Enter nums2 (space separated): 100 20 10 10 5
#output
#Maximum Distance: 2

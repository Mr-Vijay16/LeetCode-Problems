def findMin(nums):
    left = 0
    right = len(nums) - 1

    while left < right:
        mid = (left + right) // 2

        # Minimum is in the right half
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            # Minimum is in the left half including mid
            right = mid

    return nums[left]


# -------- USER INPUT --------

nums = list(map(int, input("Enter array elements: ").split()))

# Function Call
result = findMin(nums)

# Output
print("Minimum element:", result)


#sample input

# Enter array elements: 4 5 6 7 0 1 2
# Minimum element: 0
def maxRotateFunction(nums):
    n = len(nums)

    total_sum = sum(nums)

 
    F = sum(i * nums[i] for i in range(n))

    max_value = F

    # F(k) = F(k-1) + total_sum - n * nums[n-k]
    for k in range(1, n):
        F = F + total_sum - n * nums[n - k]
        max_value = max(max_value, F)

    return max_value



n = int(input("Enter number of elements: "))
nums = list(map(int, input("Enter elements: ").split()))

# Output
print("Maximum Rotation Function Value:", maxRotateFunction(nums))

#sample output

#Enter number of elements: 4
#Enter elements: 4 3 2 6

#Maximum Rotation Function Value: 26
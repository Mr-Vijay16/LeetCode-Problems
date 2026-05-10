def maximumJumps(nums, target):
    n = len(nums)

   
    dp = [-1] * n
    dp[0] = 0

    for i in range(n):
        if dp[i] == -1:
            continue

        for j in range(i + 1, n):
            if -target <= nums[j] - nums[i] <= target:
                dp[j] = max(dp[j], dp[i] + 1)

    return dp[-1]




nums = list(map(int, input("Enter array elements: ").split()))
target = int(input("Enter target value: "))


result = maximumJumps(nums, target)


print("Maximum number of jumps:", result)


#sample output
#Enter array elements: 1 2 3 4 5
#Enter target value: 1
#Maximum number of jumps: 2
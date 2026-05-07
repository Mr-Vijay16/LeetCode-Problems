def maxValue(nums):
    n = len(nums)
    ans = [0] * n

   
    max_num = max(nums)

   
    for i in range(n):
        ans[i] = max_num

    return ans



nums = list(map(int, input("Enter array elements: ").split()))


result = maxValue(nums)

# Output
print("Maximum reachable values:")
print(result)

#sample output
#Enter array elements: 1 2 3 4 5
#Maximum reachable values:
#[5, 5, 5, 5, 5]
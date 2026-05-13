def minMoves(nums, limit):
    n = len(nums)

    # Difference array
    diff = [0] * (2 * limit + 2)

    for i in range(n // 2):
        a = nums[i]
        b = nums[n - 1 - i]

        low = min(a, b) + 1
        high = max(a, b) + limit
        total = a + b

        # Initially assume 2 moves
        diff[2] += 2

        # One move range
        diff[low] -= 1
        diff[high + 1] += 1

        # Zero move at exact sum
        diff[total] -= 1
        diff[total + 1] += 1

    answer = float('inf')
    current = 0

    for s in range(2, 2 * limit + 1):
        current += diff[s]
        answer = min(answer, current)

    return answer


# -------- USER INPUT --------

nums = list(map(int, input("Enter array elements: ").split()))
limit = int(input("Enter limit value: "))

# Function Call
result = minMoves(nums, limit)

# Output
print("Minimum moves required:", result)



#sample output
#Enter array elements: 1 2 3 4 5
#Enter limit value: 2
#Minimum moves required: 2

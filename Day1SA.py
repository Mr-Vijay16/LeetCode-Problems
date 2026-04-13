# take input from user
nums = list(map(int, input("Enter numbers: ").split()))
target = int(input("Enter target: "))
start = int(input("Enter start index: "))

min_dist = 100000   # big number

# loop through array
for i in range(len(nums)):
    if nums[i] == target:
        distance = abs(i - start)
        
        if distance < min_dist:
            min_dist = distance

print("Minimum Distance:", min_dist)
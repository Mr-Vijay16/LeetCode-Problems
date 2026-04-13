#Minimum Distance to Target Element
class Solution:
    def getMinDistance(self, nums, target, start):
        min_dist = float('inf')
        
        for i in range(len(nums)):
            if nums[i] == target:
                min_dist = min(min_dist, abs(i - start))
        
        return min_dist


# 🔽 User Input Section
nums = list(map(int, input("Enter numbers: ").split()))
target = int(input("Enter target: "))
start = int(input("Enter start index: "))

# 🔽 Function Call
sol = Solution()
result = sol.getMinDistance(nums, target, start)

print("Minimum Distance:", result)
# Take input
words = input("Enter words (space separated): ").split()
target = input("Enter target word: ")
startIndex = int(input("Enter start index: "))

n = len(words)
ans = float('inf')

# Loop through words
for i in range(n):
    if words[i] == target:
        dist = abs(i - startIndex)
        ans = min(ans, dist, n - dist)

# Output result
if ans == float('inf'):
    print(-1)
else:
    print("Shortest distance:", ans)
#output:
#Enter words (space separated): hello world hello
#Enter target word: hello
#Enter start index: 1
#Shortest distance: 1
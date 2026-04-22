# Function to check if two words differ by at most 2 characters
def is_valid(q, d):
    diff = 0
    for i in range(len(q)):
        if q[i] != d[i]:
            diff += 1
        if diff > 2:
            return False
    return True

# Take input
queries = input("Enter queries (space separated): ").split()
dictionary = input("Enter dictionary words (space separated): ").split()

result = []

# Check each query
for q in queries:
    for d in dictionary:
        if is_valid(q, d):
            result.append(q)
            break

# Output
print("Output:", result)

#sample input:
# Enter queries (space separated): word note ants wood
# Enter dictionary words (space separated): wood note ant word

# Output: ['word', 'note', 'wood']
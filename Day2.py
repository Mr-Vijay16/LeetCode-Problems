# take robot positions
robots = list(map(int, input("Enter robot positions: ").split()))

# number of factories
f = int(input("Enter number of factories: "))

factories = []

for _ in range(f):
    pos, limit = map(int, input("Enter factory position and limit: ").split())
    factories.append([pos, limit])

# sort both
robots.sort()
factories.sort()

total_distance = 0
i = 0  # robot pointer

# assign robots to factories
for pos, limit in factories:
    count = 0
    
    while i < len(robots) and count < limit:
        total_distance += abs(robots[i] - pos)
        i += 1
        count += 1

print("Minimum Total Distance:", total_distance)


#output:
#Enter robot positions: 0 4 6
##Enter number of factories: 2
#Enter factory position and limit: 2 2
#Enter factory position and limit: 6 2
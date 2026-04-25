# Manhattan distance
def dist(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

# Check if we can pick k points with at least min_dist
def can(points, k, min_dist):
    selected = [points[0]]
    
    for p in points[1:]:
        ok = True
        for s in selected:
            if dist(p, s) < min_dist:
                ok = False
                break
        if ok:
            selected.append(p)
        if len(selected) == k:
            return True
    
    return False

# Main logic
def max_distance(points, k):
    points.sort()
    
    left, right = 0, 10**9
    ans = 0
    
    while left <= right:
        mid = (left + right) // 2
        
        if can(points, k, mid):
            ans = mid
            left = mid + 1
        else:
            right = mid - 1
    
    return ans


# -------- USER INPUT --------
side = int(input("Enter side length: "))
n = int(input("Enter number of points: "))

points = []
print("Enter points (x y):")
for _ in range(n):
    x, y = map(int, input().split())
    points.append([x, y])

k = int(input("Enter k: "))

# Output
print("Maximum Minimum Distance:", max_distance(points, k))

# Sample Input:
# Enter side length: 5
# Enter number of points: 4
# Enter points (x y):
# 1 1
# 2 2
# 3 3
# 4 4
# Enter k: 2
# Maximum Minimum Distance: 2
# Union-Find (Disjoint Set)

class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px != py:
            self.parent[px] = py


def min_hamming_distance(source, target, allowed_swaps):
    n = len(source)
    dsu = DSU(n)
    
    # Step 1: Group indices using DSU
    for a, b in allowed_swaps:
        dsu.union(a, b)
    
    from collections import defaultdict, Counter
    
    groups = defaultdict(list)
    
    # Step 2: Collect indices by root
    for i in range(n):
        root = dsu.find(i)
        groups[root].append(i)
    
    res = 0
    
    # Step 3: Compare frequencies inside each group
    for indices in groups.values():
        src_count = Counter(source[i] for i in indices)
        tgt_count = Counter(target[i] for i in indices)
        
        for val in src_count:
            if val in tgt_count:
                matched = min(src_count[val], tgt_count[val])
                src_count[val] -= matched
        
        res += sum(src_count.values())
    
    return res


# -------- USER INPUT --------
source = list(map(int, input("Enter source array: ").split()))
target = list(map(int, input("Enter target array: ").split()))

m = int(input("Enter number of allowed swaps: "))
allowed_swaps = []

print("Enter swap pairs (a b):")
for _ in range(m):
    a, b = map(int, input().split())
    allowed_swaps.append([a, b])

# Output
print("Minimum Hamming Distance:", min_hamming_distance(source, target, allowed_swaps))

# Sample Input:
# Enter source array: 1 2 3 4
# Enter target array: 2 1 4 5
# Enter number of allowed swaps: 2
# Enter swap pairs (a b):
# 0 1
# 2 3
# Sample Output:
# Minimum Hamming Distance: 1

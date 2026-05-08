from collections import deque, defaultdict


def is_prime(num):
    if num < 2:
        return False

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False

    return True


def minJumps(nums):
    n = len(nums)

    
    prime_map = defaultdict(list)

    for i, val in enumerate(nums):
        for p in range(2, int(val ** 0.5) + 1):
            if val % p == 0:
                if is_prime(p):
                    prime_map[p].append(i)

                while val % p == 0:
                    val //= p

        if val > 1:
            prime_map[val].append(i)

    
    queue = deque([(0, 0)]) 
    visited = set([0])

    used_primes = set()

    while queue:
        idx, jumps = queue.popleft()


        if idx == n - 1:
            return jumps


        for nxt in [idx - 1, idx + 1]:
            if 0 <= nxt < n and nxt not in visited:
                visited.add(nxt)
                queue.append((nxt, jumps + 1))

  
        val = nums[idx]

        if is_prime(val) and val not in used_primes:
            for nxt in prime_map[val]:
                if nxt not in visited:
                    visited.add(nxt)
                    queue.append((nxt, jumps + 1))

            used_primes.add(val)

    return -1


nums = list(map(int, input("Enter array elements: ").split()))


result = minJumps(nums)

# Output
print("Minimum jumps required:", result)
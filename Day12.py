# Take input
moves = input("Enter moves string (L, R, _): ")

left = 0
right = 0
blank = 0

# Count occurrences
for ch in moves:
    if ch == 'L':
        left += 1
    elif ch == 'R':
        right += 1
    else:
        blank += 1

# Maximum distance
result = abs(left - right) + blank

# Output
print("Furthest Distance:", result)

#sample output
#Enter moves string (L, R, _): L_RL__
#Furthest Distance: 4
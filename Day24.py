def rotateTheBox(box):
    m, n = len(box), len(box[0])

    # (stones fall to the right)
    for row in box:
        empty = n - 1
        for j in range(n - 1, -1, -1):
            if row[j] == '*':  # obstacle
                empty = j - 1
            elif row[j] == '#':  # stone
                row[j], row[empty] = '.', '#'
                empty -= 1

    
    result = [[None] * m for _ in range(n)]
    for i in range(m):
        for j in range(n):
            result[j][m - 1 - i] = box[i][j]

    return result



m = int(input("Enter number of rows: "))
n = int(input("Enter number of columns: "))

print("Enter box grid row by row (use #, *, . without spaces):")
box = []
for _ in range(m):
    row = list(input().strip())
    box.append(row)


rotated = rotateTheBox(box)

# Output
print("Rotated Box:")
for row in rotated:
    print("".join(row))


#sample input:
# Enter number of rows: 3
# Enter number of columns: 3
# Enter box grid row by row (use #, *, . without spaces):
# #*.
# #*.
# #*.
# Rotated Box:
# *#.
# *#.
# *#.
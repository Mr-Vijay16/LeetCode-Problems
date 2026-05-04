def rotate_image(matrix):
    n = len(matrix)

    
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    
    for row in matrix:
        row.reverse()

    return matrix



n = int(input("Enter size of matrix (n x n): "))

print("Enter matrix row by row (space separated):")
matrix = []
for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)


result = rotate_image(matrix)


print("Rotated Matrix:")
for row in result:
    print(*row)


#sample output
#Enter size of matrix (n x n): 3
#Enter matrix row by row (space separated):
#1 2 3
#4 5 6
#7 8 9
#Rotated Matrix:
#7 4 1
#8 5 2
#9 6 3


# program that replace column in matrix
n, m = int(input()), int(input())
matrix = [input().split() for _ in range(n)]
col_number=input().split()
col1=int(col_number[0])
col2=int(col_number[1])
for row in range(n):
    matrix[row][col1], matrix[row][col2] = matrix[row][col2], matrix[row][col1]
for r in range(n):
    for c in range(m):
        print(matrix[r][c], end=' ')
    print()


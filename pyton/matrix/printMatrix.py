n,m =int(input()),int(input())
matrix = [[0]*m for i in range(n)]
# print(matrix)
for i in range(n):
    for j in range(m):
        matrix[i][j] = int(input())
print(matrix)

def print_matrix(matrix, n, width=1):
    for r in range(n):
        for c in range(m):
            print(str(matrix[r][c]).ljust(width), end=' ')
        print()

def print_matrix2(matrix, n, width=1):
    for r in range(m):
        for c in range(n):
            print(str(matrix[c][r]).ljust(width), end=' ')
        print()
print_matrix(matrix, n)
print_matrix2(matrix, n)


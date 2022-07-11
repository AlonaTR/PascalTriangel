n,m=int(input()),int(input())
matrix=[]
matrix=[([0]*n) for i in range(m)]
for row in range(n):
    for col in range(m):
        matrix[col][row]=row*col
# [print(str(row).ljust(3), sep=' ') for row in matrix ]
def print_matrix(matrix, n, m, width=3):
    for r in range(n):
        for c in range(m):
            print(str(matrix[c][r]).ljust(width), end=' ')
        print()
print_matrix(matrix, n,m)
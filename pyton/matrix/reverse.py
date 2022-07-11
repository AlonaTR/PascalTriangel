n= int(input())
matrix = [input().split() for _ in range(n)]
matrix.reverse()
for r in range(n):
    for c in range(n):
        print(matrix[r][c], end=' ')
    print()
n=int(input())
matrix=[]
max=0
for _ in range(n):
    matrix.append(input().split())

for row in range(n):
    for col in range(n):
        if row > col:
            if int(matrix[row][col]) > max:
                max = int(matrix[row][col])
print(max)
print(matrix)

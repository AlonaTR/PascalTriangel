n= int(input())
matrix = [input().split() for _ in range(n)]
flag='YES'
for row in range(n):
    for col in range(n):
        if int(matrix[row][col]) != int(matrix[col][row]):
            flag='NO'
            break
print(flag)

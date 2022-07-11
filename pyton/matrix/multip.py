
num=input().split()
n,m=int(num[0]),int(num[1])
# n,m=int(input()),int(input())
matrix=[]
matrix1=[]
matrix2=[]
matrix1,matrix2=[([0]*m) for i in range(n)],[([0]*m) for i in range(n)]
for i in range(n):
        matrix1[i] = input().split()
print()
for i in range(n):
        matrix2[i] = input().split()

for row in range(n):
    for col in range(m):
        # print(matrix1[row][col],end=' ')
        # print(matrix2[row][col],end=' ')
        matrix1[row][col]=int(matrix1[row][col])+int(matrix2[row][col])
        print(matrix1[row][col],end=' ')
    print()

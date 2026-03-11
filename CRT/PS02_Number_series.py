'''''
n = int(input())
for i in range(n):
    print(i)

n = int(input())
for i in range(2,n+1,2):
    print(i)

n = int(input())
for i in range(1,n+1,2):
    print(i)

n = int(input())
a,b = 0,1
for i in range(1,n+1):
    c = a + b
    a = b
    b = c
    print(c, end=" ")

n = int(input())
for i in range(1,40):
    print(n, "x",i, "=",n*i)

n = int(input())
for i in range(1,n+1):
    print(i*i)
'''

'''
n = 4
for i in range(n):
    for j in range(n):
        print("*", end="")
    print()

n = 4
for i in range(1,n+1):
    for j in range(i):
        print('*',end=" ")
    print()
    
n = 4
for i in range(1,n+1):
    for j in range(n-i+1):
        print('*',end=" ")
    print()
    '''
n = int(input())
for i in range(1,n+1):
    ch = 65
    for j in range(i):
        print(chr(ch+j),end=" ")
    print()



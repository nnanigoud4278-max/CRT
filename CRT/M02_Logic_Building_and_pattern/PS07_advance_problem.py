''''
n = int(input())
for i in range(n):
    num = 1 
    for j in range(i+1):
        print(num, end=" ")
        num = num * (i-j) // (j+1)
    print()
'''
#Butterfly pattern
n = int(input())
for i in range(n):
    for j in range(n):
        if j<=i:
            print("*", end="")
        else:
            print(" ", end="")
    for j in range(n):
        if j<n-i-1:
            print(" ", end="")
        else:
            print("*", end="")
    print()
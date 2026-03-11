'''
n = int(input())
fact = 1
for i in range(1,n+1):
    fact *= i
print(fact)


2.write a python code to check wheather  a number is armstrong or not ?
ex : 153-->1,5,3-->(1 ** 3) + (5 ** 3) + (3 ** 3) == 153

3.write a program wheather a number is prime number or not

num = int(input("Enter a number: "))

if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print("Not a Prime number")
            break
    else:
        print("Prime number")
else:
    print("Not a Prime number")

'''

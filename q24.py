#Write a program to find the sum of first n numbers, 
#where n will be provided by the user. Eg if the user provides n=10 the output should be 55.

def sum(n):
    total=0
    for i in range(1, n):
        total+=i
    print("sum=", total)

n=int(input("enter a number")  )
sum(n)  


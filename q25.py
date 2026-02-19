#Write a program that can multiply 2 numbers provided by the user without using the * operator
def multiply(a,b):
    sum=0
    for i in range(b):
        sum+=a
    print("result=",sum)

x=int(input("Enter a num"))
y=int(input("Enter num2"))
multiply(x,y)
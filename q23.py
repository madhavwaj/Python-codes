#Write a program that will swap numbers


def swap(a,b):
    temp=a
    a=b
    b=temp
    print(a,b)


a=int(input("enter a number 1 "))    
b=int(input("enter number2"))
swap(a,b)
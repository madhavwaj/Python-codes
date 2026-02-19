#Write a program that can find the factorial of a given number provided by the user.
#3-> 3*2*1=6

def fact(n):
    pro=1
    for i in range(1,n+1):
        pro*=i
    print(pro)
n=int(input("enter"))  
fact(n)      

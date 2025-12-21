#Write a program that will check whether the number is armstrong number or not.
def arm(n):
    fact=str(len(n))
    temp=n
    sum=0

    while n>0:
        dig=temp%10
        sum=sum+dig**fact
        temp=temp//10
    if temp==n:
        print("Armstrong") 
    else:
        print("Not Arm strong")       
n=int(input("Enter a number"))      
arm(n)
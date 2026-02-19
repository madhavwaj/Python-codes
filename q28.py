#Write a program to print whether a given number is prime number or not
def prime(n):
    if n<1:
        print("not prime") 
        return
    for i in range(2,n):
        if n%i==0:
            print("not prime")
            return
        print("prime")
n=int(input("Enter a number"))    
prime(n)
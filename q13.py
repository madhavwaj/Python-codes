#Write  a program that will tell whether the given number is divisible by 3 & 6.
def divisible(num):
    if num%3==0 and num%6==0:
        print(num," is divisible by 3 and 6")

num = int(input("Enter a number"))
divisible(num)
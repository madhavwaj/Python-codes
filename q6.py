#Write a program that will tell whether the number entered by the user is odd or even.
def odd_even(num):
    if num%2==0:
        print("even")
    else:
        print("odd")
n=int(input("Enter a number"))
odd_even(n)            
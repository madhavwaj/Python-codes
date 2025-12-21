#Write a program that will tell whether the given year is a leap year or not.
def leap_yr(num):
    if (num%400==0) or (num%4==0 and num%100!=0):
        print("leap year")
    else:
        print("not leap year")
n=int(input("Enter year: "))
leap_yr(n)        
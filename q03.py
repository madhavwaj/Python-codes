#User will input (2numbers).Write a program to swap the numbers
num1 = int(input("enter a first number: "))
num2 = int(input("enter 2nd number: "))
temp=num1
num1=num2
num2=temp
print(f"After swapping, the values are: num1 = {num1}, num2 = {num2}")
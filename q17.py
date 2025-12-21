#Write a program that will take three digits from the user and add the square of each digit.

def add_square(a, b, c):
    total = a*a + b*b + c*c
    print("Sum of squares =", total)

x = int(input("Enter digit 1: "))
y = int(input("Enter digit 2: "))
z = int(input("Enter digit 3: "))

add_square(x, y, z)

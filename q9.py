#Write a program that take a user input of three angles 
#and will find out whether it can form a triangle or not.
def triangle(a,b,c):
    if a + b > c and a + c > b and b + c > a:
        print("Triangle can formed")
    else:
        print("not triangle")    


x=int(input("Enter side1 : "))
y=int(input("enter side2 : "))
z=int(input("Enter side3 : "))
triangle(x,y,z)
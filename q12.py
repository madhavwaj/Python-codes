#Write a program to find the volume of the cylinder. 
#Also find the cost when ,when the cost of 1litre milk is 40Rs.
import math

def vol_cyl(r, h):
    # volume in cubic cm
    volume = math.pi * r**2 * h  
    print("Volume (cubic cm):", volume)

    # convert cubic cm to litres (1000 cubic cm = 1 litre)
    litres = volume / 1000
    print("Volume in litres:", litres)

    # cost calculation
    cost = litres * 40
    print("Total Cost (Rs):", cost)

# user inputs
r = float(input("Enter radius (cm): "))
h = float(input("Enter height (cm): "))

vol_cyl(r, h)

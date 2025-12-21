#Write a program to find the euclidean distance between two coordinates.
import math

def euclidean_distance(x1,y1,x2,y2):
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    print(distance)

a=int(input("Enter coordinate a"))
b=int(input("Enter coordinate b"))
c=int(input("Enter coordinate c"))
d=int(input("Enter coordinate d"))   
euclidean_distance(a,b,c,d)
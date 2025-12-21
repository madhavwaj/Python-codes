#User will input (3ages).Find the oldest one

age1=int(input("Enter age of p1"))
age2=int(input("Enter age of p2"))
age3=int(input("Enter age of p3"))
if age1>age2 and age1>age3:
    print("p1 is the oldest: ")
if age2>age3 and age2>age1:
    print("p2 is the oldest: ") 
if age3>age2 and age3>age1:
    print("p3 is the oldes: ")    
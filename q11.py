#Write a program to find the simple interest when the value of principle,
#rate of interest and time period is given.
def ptr(p,t,r):
    rate = (p*r*r)/100
    print(rate)
p=int(input("Enter principle :")) 
t=int(input("Enter time : "))   
r=int(input("Enter rate : "))
ptr(p,t,r)
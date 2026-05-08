#Print all factors of a given number provided by the user.
n= int(input("Enter num"))
print("Factors are: ")
for i in range(1, n+1):
    if n%i==0:
        print(i)
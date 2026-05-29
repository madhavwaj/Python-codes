# Write a program to calculate the sum of the following series till the nth term
# 1/1! + 2/2! + 3/3! + 4/4! +…….+ n/n!
# n will be provided by the user

n= int(input("Enter a num"))
sum=0
fact=1
for i in range(1, n+1):
    fact*=i
    sum+=i/fact
print(sum)    
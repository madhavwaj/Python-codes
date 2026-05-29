# Write a program that accepts 2 numbers from the user a numerator
# and a denominator and then simplifies it
# Eg if the num = 5, den = 15 the answer should be ⅓
# Eg if the num = 6, den = 9 the answer should be ⅔

num = int(input("enter num : "))
den = int(input("enter den : "))
small=min(num, den)
for i in range(small, 0, -1):
    if num%i==0 and den%i==0:
        hcf=i
        break
num=num//hcf     
den=den//hcf     
print("Simplifies=", num,"/", den)           
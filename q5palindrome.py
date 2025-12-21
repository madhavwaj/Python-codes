#Write a program that will reverse a four digit number.
# Also it checks whether the reverse is true.
num = int(input("Enter a num: "))
sum=0
temp = num

while (temp>0):
    dig = temp%10
    sum = sum*10+dig
    temp = temp//10
print(sum)

if num==sum:
    print("palindrome number ")
else:
    print("Not palindrome")      
print(sum)
# Count the frequency of a particular character in a provided string. Eg
# 'hello how are you' is the string, the frequency of h in this string is 2.

s=input("Enter sentence: ")
ch=input("enter char: ")
count=0
for i in s:
    if i==ch:
        count=count+1
print("frequency=", count)        
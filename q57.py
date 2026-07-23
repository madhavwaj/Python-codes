#57. Write a program that can check whether a given string is palindrome or
#not.

n=input("Enter string")
z=(n[::-1])
if z==n:
    print("palindrom")
else:
    print("nt palindrome")    


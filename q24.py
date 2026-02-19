#Write a program to find the sum of first n numbers, 
# where n will be provided by the user. Eg if the user provides n=10 the output should be 55.

def sum_n(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    print("Sum =", total)

n = int(input("Enter n: "))
sum_n(n)

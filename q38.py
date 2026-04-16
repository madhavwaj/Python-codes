#Take a number from the user and find the number of digits in it.

n = int(input("enter a num: "))
count = 0

# Special case
if n == 0:
    count = 1
else:
    n = abs(n)   # handle negative numbers

    while n > 0:
        n = n // 10   # update n
        count += 1

print("number of digits =", count)
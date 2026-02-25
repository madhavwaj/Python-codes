#User will provide 2 numbers you have to find the HCF of those 2 numbers
def hcf(a, b):
    small = min(a, b)
    for i in range(small, 0, -1):
        if a % i == 0 and b % i == 0:
            print("HCF =", i)
            break

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

hcf(x, y)
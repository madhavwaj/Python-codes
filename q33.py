#User will provide 2 numbers you have to find the by LCM of those 2 numbers
def lcm(a, b):
    # find HCF first
    x, y = a, b
    while y != 0:
        x, y = y, x % y
    hcf = x

    lcm_value = (a * b) // hcf
    print("LCM =", lcm_value)

n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))

lcm(n1, n2)
#Print all the armstrong numbers in the range of 100 to 1000
def armstrong():
    for n in range(100, 1000):
        temp = n
        total = 0
        power = len(str(n))

        while temp > 0:
            digit = temp % 10
            total += digit ** power
            temp = temp // 10

        if total == n:
            print(n)

armstrong()
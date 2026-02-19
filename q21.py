def cm_to_feet(cm):
    return cm / 30.48

def km_to_miles(km):
    return km * 0.62

def usd_to_inr(usd):
    return usd * 83

while True:
    print("\nMenu")
    print("1. cm to feet")
    print("2. km to miles")
    print("3. USD to INR")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        cm = float(input("Enter value in cm: "))
        print("Feet =", cm_to_feet(cm))

    elif choice == 2:
        km = float(input("Enter value in km: "))
        print("Miles =", km_to_miles(km))

    elif choice == 3:
        usd = float(input("Enter value in USD: "))
        print("INR =", usd_to_inr(usd))

    elif choice == 4:
        print("Exiting program")
        break

    else:
        print("Invalid choice")

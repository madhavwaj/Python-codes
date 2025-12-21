def profit_loss(cp, sp):
    if cp > sp:
        loss = cp - sp
        print("Loss of", loss)
    elif sp > cp:
        profit = sp - cp
        print("Profit of", profit)
    else:
        print("No Profit, No Loss")

cp = int(input("Enter Cost Price: "))
sp = int(input("Enter Selling Price: "))

profit_loss(cp, sp)

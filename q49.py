# 49. Write a program that keeps on accepting a number from the user until
# the user enters Zero. Display the sum and average of all the numbers.
total =0
count=0
while True:
    num=int(input("enter num 0 to stop"))
    if num==0:
        break
    count+=1
    total+=num

if count>0:
    print("sum=",total)
    print("avg",total/count)
else:
    print("no num")    
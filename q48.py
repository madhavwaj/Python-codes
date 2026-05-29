# 48. The natural logarithm can be approximated by the following series.If x is input through the keyboard,
# write a program to calculate the
# sum of the first seven terms of this series.
# (x-1)/x + 1/2·((x-1)/x)² + 1/3·((x-1)/x)³ + ... + 1/7·((x-1)/x)⁷
x = int(input("enter num"))
sum=0
base=((x-1)/x)
for i in range(1, 8):
    sum+=(1/i)*(base**i)
print(sum)    

 
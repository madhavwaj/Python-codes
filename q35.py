#Print the first 20 numbers of a Fibonacci series
#0,1,1,2,3,5,8
def fib(n):
    a=0
    b=1
    for i in range(n):
        print(a)
        a,b=b,a+b
fib(20)        
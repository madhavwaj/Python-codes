#Write a program that will give you the in hand salary after deduction of 
# HRA(10%),DA(5%),PF(3%), and tax(if salary is between 5-10 lakh–10%),(11-20lakh–20%),
#(20< _   – 30%)
# (0-1lakh print k).

def salary_calc(n):
    if n <=100000:
        print("k")
        return

    hra = n*0.10
    da = n*0.05
    pf = n*0.03
    
    gross_salary= n-(hra+da+pf)

    if 500000 <= n <= 1000000:
        tax = 0.10*gross_salary
    elif 1100000 <= n <= 2000000:
        tax = 0.10 *gross_salary
    elif n>2000000:
        tax = 0.10*gross_salary
    else:
        tax = 0

    inhandsal= gross_salary-tax
    print("In-hand salary:", inhandsal)    




n=int(input("Enetr salary in lakhs"))
salary_calc(n)
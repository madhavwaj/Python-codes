#Write a program to find the compound interest 
def compound_interest(P,R,T):
    amt=P*(1+R/100)**T
    ci=amt-P
    print("compound ", amt)
    print("amt", amt)
P=int(input("Enter principal")) 
R=int(input("Enter Rate"))  
T=int(input("Enter Time")) 
compound_interest(P,R,T)
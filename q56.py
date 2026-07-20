#56. Write a program which can remove a particular character from a string.
def name(n1,n2):
    result=""
    for i in n1:
        if i!=n2:
            result=result+i
    print(result)
n1=input("string -> ")
n2=input("what u wanna remove ->")            
name(n1,n2)
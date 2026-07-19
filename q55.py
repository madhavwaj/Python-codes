#55. Count the number of vowels in a string provided by the user.
def word(name):
    count=0
    for i in name:
        if i in 'aeiouAEIOU':
            count=count+1
    print(count)  
name=input("input name = ")    
word(name)      

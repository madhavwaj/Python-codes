#54.Find the index position of a particular character in another string.

def posidx(sen, ch):
    for i in range(len(sen)):
        if sen[i] == ch:
            print(i)

sen = input("Enter string: ")
ch = input("Enter character: ")

posidx(sen, ch)

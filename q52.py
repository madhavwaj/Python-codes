#Extract username from a given email.
#Eg if the email is nitish24singh@gmail.com then the username
#should be nitish24singh

email = input("Enter email: ")

username = ""

for ch in email:
    if ch == "@":
        break
    username += ch

print("Username =", username)
#User inputs information
f = open("Usernames and passwords.txt","a")
name = input("Please enter your name: ")
age = input("Please enter your age: ")
password = input("Please enter a password: ")
username = ""
for i in range(3): #Loops for the first 3 letters of the name
    username += (name[i])
username += age
print(username)


if username in open("Usernames and passwords.txt").read():
    print("Sorry this username is taken.")
    exit()

else:
    print("Account has been made.")
    
f.write("User: "+username+"  Password:"+password+"\n")
f.close


#User selects subject
subject = input("Please select a subject: ").lower()
if subject == "music":
    print("You have selected music")
elif subject == "history":
    print("You have selected history")
elif subject == "computer science" or "computing":
    print("You have selected computer science")

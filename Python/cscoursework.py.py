#login or create an account
user = ""
accs = open("accs.txt","r")
look = accs.read()
look = look.split("\n")
accs.close()

accs = open("accs.txt","w")
accs.close

def intro():
    intq = input("Do you already have an account? Press y if yes; n if no ")
    if intq.lower()=="y":
        print ("Login")
    elif intq.lower()=="n":
        print ("Create an account")
        func1()
    else:
        intro()

#makeuser
def func1():
    nameq = input("Please enter your name: ")
    name = ""
    for i in range(3):
        name+=(nameq[i])
    age = input("Please enter your age: ")
    year = input("Please enter your year group: ")
    user = name + age
    #first check against accs

    
    #then add if user not taken
    print ("Your username is: "+user)
    acc = open("%s.csv"%user,"w")
    acc.write(user+" \n")
    acc.close

    func2()

#makepass
def func2():
    pasq = input("Please enter a password: ")
    pasr = input("Please re-enter the password: ")
    if pasq == pasr:
        acc = open("%s.csv"%user,"a")
        acc.write(pasr)
        acc.close
    elif pasq != pasr:
        print("The passwords you entered did not match")
        func2()

#login
def func3():
    userq = input("What is your username? ")
    passq = input("What is your password? ")

    gogo = ""
    if userq == user:
        gogo += "a"
    if passq == pasr:
        gogo += "a"
    if gogo == "aa":
        print("func4()")
    if gogo != "aa":
        print("Either the username or password is incorrect; please try again.")
        func3()

intro()

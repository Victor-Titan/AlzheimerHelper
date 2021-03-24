import aiml
import os
import sqlite3

kernel = aiml.Kernel()
conn = sqlite3.connect('users.db')
cur = conn.cursor()

if os.path.isfile("bot_brain.brn"):
    kernel.bootstrap(brainFile = "bot_brain.brn")
else:
    kernel.bootstrap(learnFiles = "std-startup.xml", commands = "load aiml b")
    kernel.saveBrain("bot_brain.brn")

row = 0

def register(name, address, phno, dad, mom, emcon, guardian, age):
    kernel.setPredicate('name', name)
    kernel.setPredicate('address', address)
    kernel.setPredicate('phno', phno)
    kernel.setPredicate('fname', dad)
    kernel.setPredicate('mom', mom)
    kernel.setPredicate('emcon', emcon)
    kernel.setPredicate('guardian', guardian)
    kernel.setPredicate('age', age)

while True:
    c = input("1 to Login\n2 to Register\n")
    if(c=="1"):
        user = input("Enter user id: ")
        pwd = input("Enter password: ")
        cur.execute("SELECT * FROM info WHERE id=? ",(user,))
        row = cur.fetchone()
        if(row[1]==pwd):
            kernel.setPredicate('name',row[2])
            kernel.setPredicate('address',row[3])
            kernel.setPredicate('phno',row[4])
            kernel.setPredicate('fname',row[5])
            kernel.setPredicate('mom',row[6])
            kernel.setPredicate('emcon',row[7])
            kernel.setPredicate('guardian',row[8])
            kernel.setPredicate('age',row[9])
            break
        else:
            print("Wrong credentials! Try again!\n")
        
    elif(c=="2"):
        id = input("Enter id: ")
        name=input("Enter name: ")
        pwd=input("Enter password: ")
        address=input("Enter address: ")
        phno=input("Enter phone number: ")
        dad=input("Enter dad: ")
        mom=input("Enter mom: ")
        emcon=input("Enter emcon: ")
        guardian=input("Enter guardian's name: ")
        age=input("Enter age: ")
        register(name, pwd, address, phno, dad, mom, emcon, guardian, age)
        break
    
    else:
        print("Wrong choice! Try again!\n")

#name = input("Enter your name: ")
#kernel.setPredicate('name',name)
while True:
    message = input(">>")
    if message == "quit" or message == "exit":
        conn.close()
        exit()
    else:
        bot_response = kernel.respond(message)
        print (">>"+bot_response)
import aiml

kernel = aiml.Kernel()

kernel.learn("basic.aiml")

while True:
    message = input(">>")
    if message == "quit" or message == "exit":
        exit()
    else:
        bot_response = kernel.respond(message)
        print (">>"+bot_response)
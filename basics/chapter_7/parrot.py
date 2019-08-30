prompt  = "Tell me something, I'll repeat it back to you: "
prompt += "\nEnter 'quit' to end the program. "

active = True

while active:
    message = input (prompt)

    if message == "quit":
        active = False
    else:
        print (message)

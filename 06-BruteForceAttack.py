#This is a password check simulation
attempts = 5
password = 'skibidi'
#Defines the attempts and password
ask = input("What is the password:")
#Asks user for input
while ask.lstrip() != password:
    attempts = attempts - 1
#Subtracts attempts if user inputs the wrong input.
    if attempts == 0:
        print('The supreme leader, xin jin ping has assigned your execution in 2 hours')
        break
    print(str(attempts) + " Attempts left")
    ask = input("What is the password:")
#Checks if user reached the attempts limit, if they did it ends the program. If there are some left it shows attempts left to user and asks to give input again.
else:
    print("correct")
#Assures user they got the input correctly.













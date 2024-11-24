#Takes the user input's selected month number and gives the total days.
dictionary ={1: 31,2 : 28, 3: 31, 4 : 30, 5 : 31, 6 : 30, 7 : 31, 8 : 31, 9 : 30,  10 : 31,  11 : 30,  12 : 31}
#Uses dictionary to store and list data all in one.
key = int(input('Enter A Month Number:'))
#Asks user to input a month number
while key not in dictionary:
    key = int(input('Please input a valid month number:'))
#Verifies if user input is in the list and if true prints the days, if not it asks again and then outputs the days.
#if february is inputted it checks if the user is asking for the leap year or not
if key == 2:
    ask_2 = (input("Is this February a leap year? Yes or No:"))
    if ask_2.lstrip().capitalize() == "YES":
        print("29")
    else:
        print("28")
    exit()
#checks input and outputs month numbers
if key in dictionary:
    print(dictionary.get(key))
    exit()


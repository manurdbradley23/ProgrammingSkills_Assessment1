#Takes the user input's selected month number and gives the total days.
dictionary ={'1': 31,'2': 28,'3': 31,'4': 30,'5': 31,'6': 30,'7': 31,'8': 31,'9': 30, '10': 31, '11': 30, '12': 31}
#Uses dictionary to store and list data all in one.
key = input('Enter A Month Number:')
#Asks user to input a month number
if key in dictionary:
    print(dictionary.get(key))
else:
    ask = input('Please input a valid month number:')
    print(dictionary.get(ask))

if key == 2
    ask
#Verifies if user input is in the list and if true prints the days, if not it asks again and then outputs the days.

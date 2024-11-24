#Searches person and returns said name
names = ["Jake","Zac","Ian", "Ron","Sam","Dave"]
#Data stored in a list
ask = input("Input a name:")
ask = names.index(ask)
search = names[ask]
print(search)
#Checks if input is in the list

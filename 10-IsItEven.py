#first even or odd function computes if number is even or odd
def even_or_odd(number):
        if number % 2 == 0:
           return "It's even"
        else:
           return "It's odd"
#main function asks for input then passes input to the first function. it then prints out the if its even or odd.
def main():
  skibidi_number = int(input("Input a skibidi number:"))
  pass_number = even_or_odd(skibidi_number)
  print(pass_number)

main()

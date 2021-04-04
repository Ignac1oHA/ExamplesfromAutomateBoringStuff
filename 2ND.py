result = 2 + 3 * 6
print(result)

Compoound = 'Alice' + 'bob'
print(Compoound)

Added = 'Alice' + str(5)
print(Added)

Multiplied ='Alice' * 5
print(Multiplied)

spam = 40
print(spam)
eggs = 2
print(spam + eggs)
spam=spam + 5
print(spam)

# This program says hello and asks for your name
print('Hello world')
print('What´s your name?')    # ask for their name
myname = input()
print('It is good to meet you' + myname)
print('The lenght of your name is:')
print(len(myname))
print('What´s your age?')    # Ask for their age
myage = input()
if myage < str(18):
    print("You are not allowed to buy beer")
else:
    print("Welcome to the Bottle-O, a beer?")
print('You will be ' + str(int(myage) + 1) + " in a year")

#!/usr/bin/python3
  
"""Random Spongebob Quote Generator"""

# import required packages
import random


# to open + read  all contents of quotes file
q = open("quotes.txt", "r")
quotes = q.readlines()
# to return randomly selected quote
randomQuote = random.choice(quotes)


# define a function to create MoCkAsE for quotes generated
def myfunc1(my_string):
    result = ''
    for i in range(0, len(my_string)):
        if i % 2 == 0:
            result += my_string[i].upper()
        else:
            result += my_string[i].lower()
    print(result)


# to open + read txt files
file = open("spongebob.txt", 'r')
content_of_file = file.read()

file = open("greeting.txt", "r")
content_of_file2 = file.read()
print(content_of_file2)
print("Are you ready?")

file = open("squidward.txt", "r")
content_of_file3 = file.read()


# loop to prompt for quotes + exit of program
while True:

    prompt = input("").lower()

    if prompt == "y" or prompt == "yes" or prompt == "Y":
        print("\n\n\n---------------------------------------------------------------")
        # output quotes with MoCkAsE function 
        myfunc1("\n" + random.choice(quotes))
        # to print spongemock ascii
        print(content_of_file)
        print("Want to hear another?")

    elif prompt == "n" or prompt == "N" or prompt == "no":
        print(content_of_file3)
        exit()

    else:
        # output when human error is made
        print("\n\nBarnacles! That's an invalid entry. [y/n]\n\n")


print("*^*^*^*^^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*")                                                               
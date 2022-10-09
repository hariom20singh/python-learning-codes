# Python program to generate and match
# the string from all random strings
# of same length

# Importing string, random
# and time modules
import string
import random
import time

# all possible characters including
# lowercase, uppercase and special symbols
possibleCharacters = string.ascii_lowercase + string.digits + string.ascii_uppercase + ' ., !?;:'

# string to be generated
t = "tytgj"

# To take input from user
# t = input(str("Enter your target text: "))

attemptThis = ''.join(random.choice(possibleCharacters)
                    for i in range(len(t)))
attemptNext = ''

completed = False
iteration = 0

# Iterate while completed is false
while completed == False:
    print(attemptThis)

    attemptNext = ''
    completed = True

    # Fix the index if matches with
    # the strings to be generated
    for i in range(len(t)):
        if attemptThis[i] != t[i]:
            completed = False
            attemptNext += random.choice(possibleCharacters)
        else:
            attemptNext += t[i]

    # increment the iteration
    iteration += 1
    attemptThis = attemptNext
    time.sleep(0.1)

# Driver Code
print("Target matched after " +
      str(iteration) + " iterations")

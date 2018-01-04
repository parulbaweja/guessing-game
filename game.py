"""A number-guessing game."""

import random

print "Howdy, what's your name?"
name = raw_input("(type in your name)")
print "{name}, I'm thinking of a number between 1 and 100".format(name=name)
# print "{}, I'm thinking of a number between 1 and 100".format(name)
print "Try to guess my number"

num = random.randint(1, 100)
print num

num_guesses = 0

while True:
    guess = raw_input("Your guess?")
    

    try:
        guess = int(guess)
    except ValueError:
        print "That's not a number! Try again with a valid number."
        continue

    
    if guess < 1 or guess > 100:
        print "That's not between 1 and 100! Try again with a valid number."
        continue

    num_guesses += 1

    if guess > num:
        print "Your guess was too high, try again."
    elif guess < num:
        print "Your guess was too low, try again."
    else:
        response = "Well, done, {name}! You found my number in {n} tries!"
        print response.format(name=name, n=num_guesses)
        # response = "Well, done, {}! You found my number in {} tries!".format(name, num_guesses)
        break

"""A number-guessing game."""

import random

print "Howdy, what's your name?"
name = raw_input("(type in your name)")
print "{name}, I'm thinking of a number between 1 and 100".format(name=name)
print "Try to guess my number"

num = random.randint(1, 100)
num_guesses = 1

while True:
    guess = raw_input("Your guess?")
    guess = int(guess)
    if guess != num:
        if guess > num:
            print "Your guess was too high, try again."
        else:
            print "Your guess was too low, try again."
        num_guesses += 1
    else:
        response = "Well, done, {name}! You found my number in {n} tries!"
        print response.format(name=name, n=num_guesses)
        break
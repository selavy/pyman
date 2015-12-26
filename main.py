#!/usr/bin/env python

import random

def get_guess():
    guess = str(raw_input("Guess a letter: "))
    if not guess or len(guess) > 1:
        raise Exception("You were only supposed to enter a letter!")
    letter = guess[0]
    letter = letter.lower()
    if letter < 'a' or letter > 'z':
        raise Exception("Letter entered not valid: " + letter)
    return letter


def generate_word():
    words = ["hello", "goodbye", "mystery"]
    return random.choice(words)


def print_man(misses):
    if misses == 0:
        print """
    =====
    |   |
    |
    |
    |
    |
---------"""
    elif misses == 1:
        print """
    =====
    |   |
    |   0
    |
    |
    |
---------"""
    elif misses == 2:
        print """
    =====
    |   |
    |   0
    | /[ ]\\
    |
    |
---------"""
    elif misses == 3:
        print """
    =====
    |   |
    |   0
    | /[ ]\\
    |  [ ]
    |
---------"""
    elif misses == 4:
        print """
    =====
    |   |
    |   0
    | /[ ]\\
    |  [ ]
    |  /
---------"""
    else:
        print """
    =====
    |   |
    |   0
    | /[ ]\\
    |  [ ]
    |  / \\
---------"""


def main():
    word = generate_word()
    state = ['_'] * len(word)
    letters = []
    guesses = 0
    misses = 0
    #print "The word is: ", word
    while misses < 5:
        print_man(misses)
        print "Guessed letters: ", ','.join(letters), "\n"
        print ' '.join(state)
        guess = get_guess()
        print "guess was: ", guess
        letters.append(guess)
        guesses += 1
        guessed_correct = False
        for i, letter in enumerate(word):
            if letter == guess:
                state[i] = guess
                guessed_correct = True
        if not guessed_correct:
            print "Miss!"
            misses += 1
        elif ''.join(state) == word:
            break
    print_man(misses)
    print ' '.join(state)
    if misses < 5:
        print "You won!"
    else:
        print "You lost!"
        print "The word was: ", word

if __name__ == '__main__':
    main()
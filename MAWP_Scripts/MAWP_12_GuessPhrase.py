# This script will guess a phrase using a genetic algorithm

# Source code/inspiration/software
    # Math Adventures with Python by Peter Farrell, Chapter 12+
    # Made with Mu 1.0.3 in November 2021

# Libraries needed to run this script
import random                                               # https://docs.python.org/3/library/random.html
import time                                                 # helps with code optimization by timing our script's run time

start_time = time.time()                                    # start the script runtime clock

# Phrase variables and data
target_phrase = "Alaska weather is never boring; it is currently (-)8F !"
phrase_space = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.,;?!-+()"

# Guess function
def guess_phrase():
    """"creates a list of characters as long as the target_phrase"""
    charList = []                                           # charList starts with no characters 
    for i in range(len(target_phrase)):                     # loop over as many times as there are characters in target_phrase 
        charList.append(random.choice(phrase_space))        # adds a random character from phrase_space into charList with each loop
    return charList                                         # return populated charList after loop ends

# Fitness function:
def fitness(myList):
    """evaluates the fitness by comparing myList to target_phrase"""
    matches = 0                                             # the counter, matches, starts at zero
    for i in range(len(target_phrase)):                     # loop over as many times as there are characters in target_phrase
        if myList[i] == target_phrase[i]:                   # evaluates character by character for matches
            matches += 1                                    # add 1 for each match, higher scores are closer to the target_phrase
    return matches                                          # return match count after loop ends

# Mutation function
def mutate(myList):
    """applies a random change to a character in myList"""
    newList = list(myList)
    new_letter = random.choice(phrase_space)                # randomly choose a letter from phrase_space
    index = random.randint(0, len(target_phrase)-1)         # randomly choose a number to be the index of letter to be replaced
    newList[index]= new_letter                              # set new_letter character at the index
    return newList

# Main function
def main():
    """create bestList, execute guess/fitness/mutate functions"""

    # set things into motion
    random.seed()                                           # seed value (starting #) for the random number generator
    bestList = guess_phrase()                               # generate guesses
    bestScore = fitness(bestList)                           # evaluate the fitness of the guesses
    guesses = 0                                             # the counter, guesses, starts at zero

    # loop through the mutation & fitness functions
    while True:
        guess = mutate(bestList)
        guessScore = fitness(guess)
        guesses =+ 1

        # checkpoint
        if guessScore <= bestScore:
            continue

        # if newList is fit, display, and break loop
        print(''.join(guess), guessScore, guesses)
        if guessScore == len(target_phrase):
            break

        # otherwise keep going
        bestList = list(guess)
        bestScore = guessScore
        
    end_time = time.time()                                  # stop the script runtime clock & display the results
    print("\nSpeed_check: script run time is {} seconds".format(end_time - start_time))

if __name__ == "__main__":                                  # when the if statement evaluates True, main() is executed
    main()

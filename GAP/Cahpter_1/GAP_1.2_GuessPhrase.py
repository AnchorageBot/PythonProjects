# This script will attempt to guess a phrase using a genetic algorithm

# Source code/inspiration/software
    # Genetic Algorithms with Python by Clinton Sheppard, Chapter 1, Example 2+
    # Made with Mu 1.0.3 in November 2021

# Libraries needed to run this script
import random
import datetime

# Gene set aka the problem space
geneSet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#. 1234567890"

# Target phrase to solve
target = " Hello World 1.1 !"

# Guess function
def generate_parent(length):
    """generate a random string from the gene set"""
    genes = []                                              # guess list
    while len(genes) < length:                              # loop through list until condition is satisfied
        sampleSize = min(length - len(genes), len(geneSet))
        genes.extend(random.sample(geneSet, sampleSize))    # extend appends multiple items to a list
    return ''.join(genes)                                   # join creates new string with joined values

# Fitness function
def get_fitness(guess):
    """evaluate the fitness of the guess"""
    return sum(1 for expected, actual in zip(target, guess) if expected == actual) # zip iterates over two lists simultaneously

# Mutation function
def mutate(parent):
    """create a new guess via random mutation of the old guess"""
    index = random.randrange(0,len(parent))                 # returns random element from the range
    childGenes = list(parent)
    newGene, alternate = random.sample(geneSet, 2)          # sample takes a random sample w/o replacement
    childGenes[index] = alternate if newGene == childGenes[index] else newGene
    return ''.join(childGenes)

# Display function
def display(guess):
    """display the progress of the genetic algorithm"""
    timeDiff = datetime.datetime.now() - startTime
    fitness = get_fitness(guess)
    print("{}\t{}\t{}".format(guess, fitness, timeDiff))

# Main program
random.seed()
startTime = datetime.datetime.now()
bestParent = generate_parent(len(target))
bestFitness = get_fitness(bestParent)
display(bestParent)

# While loop
while True:
    child = mutate(bestParent)
    childFitness = get_fitness(child)
    if bestFitness >= childFitness:
        continue
    display(child)
    if childFitness >= len(bestParent):
        break
    bestFitness = childFitness
    bestParent = child

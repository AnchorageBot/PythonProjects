# This script will attempt to maximize weights using a genetic algorithm

# Source code/inspiration/software
    # Impractical Python Projects by Lee Vaughn, Chapter 7, Project 13+
    # Made with Mu 1.0.3 in November 2021

# Libraries needed to run this script
import time
import random
import statistics

# Constants (weights are in grams)
GOAL = 50000
NUM_RATS = 47
INITIAL_MIN_WT = 200
INITIAL_MAX_WT = 600
INITIAL_MODE_WT = 300
MUTATE_ODDS = 0.01
MUTATE_MIN = 0.5
MUTATE_MAX = 1.2
LITTER_SIZE = 8
LITTERS_PER_YEAR = 10
GENERATION_LIMIT = 500

# Ensure even number for breeding pairs
if NUM_RATS % 2 != 0:
    NUM_RATS += 1

# Population creation function
def populate(num_rats, min_wt, max_wt, mode_wt):
   """initialize population with a triangular weight distro"""
   return[int(random.triangular(min_wt, max_wt, mode_wt)) for i in range(num_rats)]

# Fitness function
def fitness(population, goal):
    """measure fitness by comparing attribute mean vs target"""
    avg = statistics.mean(population)
    return avg/goal
    
# Selection function
def select(population, to_retain):
    """Retain those that meet criteria"""
    sorted_population = sorted(population)
    to_retain_by_sex = to_retain//2
    members_per_sex = len(sorted_population)//2
    females = sorted_population[:members_per_sex]
    males = sorted_population[members_per_sex:]
    selected_females = females[-to_retain_by_sex:]
    selected_males = males[-to_retain_by_sex:]
    return selected_males, selected_females
    
# New generation function
def breed(males, females, litter_size):
    """Repopulate by crossing over aka recombining genes"""
    random.shuffle(males)
    random.shuffle(females)
    children = []
    for male, female in zip(males, females):
        for child in range(litter_size):
            child = random.randint(female,male)
            children.append(child)
    return children

# Mutation function
def mutate(children, mutate_odds, mutate_min, mutate_max):
    """Randomize weights using input odds & fractional changes"""
    for index, rat in enumerate(children):
        if mutate_odds >= random.random():
            children[index] = round(rat*random.uniform(mutate_min, mutate_max))
    return(children)

# Main function
def main():
    """Initialize population, select, breed, mutate, and display results"""
    generations = 0
    
    parents = populate(NUM_RATS, INITIAL_MIN_WT, INITIAL_MAX_WT, INITIAL_MODE_WT)
    print("initial population weights ={}".format(parents))
    popl_fitness = fitness(parents, GOAL)
    print("initial population fitness ={}".format(popl_fitness))
    print("number to retain ={}".format(NUM_RATS))
    
    avg_wt =[]
    
    while popl_fitness < 1 and generations < GENERATION_LIMIT:
        selected_males, selected_females = select(parents, NUM_RATS)
        children = breed(selected_males, selected_females, LITTER_SIZE)
        children = mutate(children, MUTATE_ODDS, MUTATE_MIN, MUTATE_MAX)
        parents = selected_males + selected_females + children
        popl_fitness = fitness(parents, GOAL)
        print("Generation {} fitness = {:.4f}".format(generations, popl_fitness))
       
        avg_wt.append(int(statistics.mean(parents)))
        generations +=1
        
    print("average weight per generation = {}".format(avg_wt))
    print("\nnumber of generations = {}".format(generations))
    print("number of years = {}".format(int(generations / LITTERS_PER_YEAR)))
    
# Run the genetic algorithm
if __name__ == '__main__':
    """Conditional statement for running the program"""
    start_time = time.time()
    main()
    end_time = time.time()
    duration = end_time - start_time
    print("\nRuntime for this program was {} seconds.".format(duration))

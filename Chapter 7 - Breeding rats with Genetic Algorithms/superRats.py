"""model a genetic algorithm by simulating a world where a rats fitness is 
    proportional to their weight"""

import time
import random
import statistics

# initial declaration of CONSTANTS (in grams)
GOAL = 5000 
NUM_RATS = 20
INITIAL_MIN_WT = 200 
INITIAL_MAX_WT = 600
INITIAL_MODE_WT = 300
MUTATE_ODDS = 0.01
MUTATE_MIN = 0.5
MUTATE_MAX = 1.2
LITTER_SIZE = 8
LITTERS_PER_YEAR = 10
GENERATION_LIMIT = 500

# ensure even number of rats for breeding pairs
if NUM_RATS % 2 != 0:
    NUM_RATS += 1
    
def populate(num_rats, min_wt, max_wt, mode_wt):
    """Initialize a population with a triangular distribution of weights."""
    return [int(random.triangular(min_wt, max_wt, mode_wt)) for i in range(num_rats)]

def fitness(population, goal):
    """Measure population fitness based on an attribute mean vs target.
    Expressed in percentages"""
    ave = statistics.mean(population)
    return ave / goal

def select(population,toRetain):
    """Cull a population to retain only a specified number of members"""
    sortedPopulation = sorted(population)
    toRetainBySex = toRetain // 2
    membersPerSex = len(sortedPopulation)//2
    females = sortedPopulation[:membersPerSex]
    males = sortedPopulation[membersPerSex:]
    selectedFemales = females[-toRetainBySex:]
    selectedMales = males[-toRetainBySex:]
    return selectedMales, selectedFemales 

def breed(males,females,litterSize):
    """Crossover genes among members (weights) of a population."""
    random.shuffle(males)
    random.shuffle(females)
    children = []
    for male, female in zip(males,females):
        for child in range(litterSize):
            child = random.randint(female,male)
            children.append(child)
    return children

def mutate(children, mutateOdds, mutateMin, mutateMax):
    """Randomly alter rat weights using input odds & fractional changes."""
    for index, rat in enumerate(children):
        if mutateOdds >= random.random():
            children[index] = round(rat * random.uniform(mutateMin,mutateMax))
    return children

def main():
    """Initialize population, select, breed, and mutate, display results."""
    generations = 0
    parents = populate(NUM_RATS,INITIAL_MIN_WT,INITIAL_MAX_WT,INITIAL_MODE_WT)
    print("initial population weights = {}".format(parents))
    poplFitness = fitness(parents, GOAL)
    print("initial population fitness = {}".format(poplFitness))
    print("number to retain = {}".format(NUM_RATS))
    aveWt = []
    
    while poplFitness < 1 and generations < GENERATION_LIMIT:
        selectedMales, selectedFemales = select(parents, NUM_RATS)
        children = breed(selectedMales, selectedFemales, LITTER_SIZE)
        children = mutate(children, MUTATE_ODDS, MUTATE_MIN, MUTATE_MAX)
        parents = selectedMales + selectedFemales + children
        poplFitness = fitness(parents, GOAL)
        print("Generation {} fitness = {:.4f}".format(generations,
                                                      poplFitness))
        aveWt.append(int(statistics.mean(parents)))
        generations += 1 
    print("average weight per generation = {}".format(aveWt))
    print("\nnumber of generations = {}".format(generations))
    print("number of years = {}".format(int(generations / LITTERS_PER_YEAR)))

if __name__ == '__main__':
    startTime = time.time()
    main()
    endTime = time.time()
    duration = endTime - startTime
    print("\nRuntime for this program was {} seconds.".format(duration))
    input()
    
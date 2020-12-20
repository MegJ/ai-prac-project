from random import random, sample, shuffle
from program_tree import PT
from fitness_function import FitnessFunction, FitnessFunction2
import operator
from copy import deepcopy

TREE_DEPTH = 6
P_NON_TERMINAL = 0.6
P_MUTATION = .03
GENERATIONS = 20
INITIAL_POPULATION = 60

def PTCI(depth, depth_bound, terminals, operations, p_non_terminal):
    if depth == depth_bound:
        return PT(sample(terminals,1)[0])
    if random() < p_non_terminal:
        new_tree = PT(sample(operations, 1)[0])
        new_tree.add_left(PTCI(depth + 1, depth_bound, terminals, operations, p_non_terminal))
        new_tree.add_right(PTCI(depth + 1, depth_bound, terminals, operations, p_non_terminal))
        return new_tree
    return PT(sample(terminals,1)[0])
            
def generate_initial_population(n, depth_bound, terminals, operations, p_non_terminal):
    populations = []
    while(len(populations) < n):
        tree = PTCI(0, depth_bound, terminals, operations, p_non_terminal)
        populations.append(tree)
    return populations


def run_generation(population, terminals, operations, fitness_function, p_mutation, n):

    print("running generation " + str(n))

    fitness_seeds = sample(set(range(100)), 25)
    population_fitness = [(fitness_function.get_fitness(program, fitness_seeds), program) for program in population]
    population_fitness.sort(key = operator.itemgetter(0), reverse = True)
    tree = population_fitness[0][1]

    population = population_fitness[0:(len(population)//2)]
    new_population = []
    
    avg_fitness = 0
    avg_depth = 0
    shuffle(population)
    for i in range(len(population)// 2):
        f1, tree1 = population[2 * i]
        f2, tree2 = population[(2 * i) + 1]
        new_tree1 = deepcopy(tree1)
        new_tree1.crossover(deepcopy(tree2.get_subtree()), terminals, operations)
        new_tree2 = deepcopy(tree2)
        new_tree2.crossover(deepcopy(tree1.get_subtree()), terminals, operations)
        new_population.append(tree1)
        new_population.append(tree2)
        new_population.append(new_tree1)
        new_population.append(new_tree2)
        avg_fitness += f1
        avg_fitness += f2
        avg_depth += tree1.size
        avg_depth += tree2.size

    for p in new_population:
        p.mutate(p_mutation, terminals, operations)
    
    return new_population
    
def run_simulation(n,generations, terminals, operations, p_mutation):
    fitness_seeds = set(range(200))
    fitness_function = FitnessFunction(fitness_seeds, terminals)
    
    initial_population = generate_initial_population(n, TREE_DEPTH, terminals, operations, P_NON_TERMINAL)

    for i in range(generations):
        initial_population = run_generation(initial_population, terminals, operations, fitness_function, p_mutation, i)
    
    fitness_seeds = set(range(100))
    population_fitness = [(fitness_function.get_fitness(program, fitness_seeds), program) for program in initial_population]
    population_fitness.sort(key = operator.itemgetter(0), reverse = True)

    return population_fitness[0:10]
    
    
terminals = list(range(-50, 50))

for i in range(100):
    terminals.append("x")

operations = ["+", "*", "*"]

final_population = run_simulation(INITIAL_POPULATION, GENERATIONS, terminals, operations, P_MUTATION)

for fitness, p in final_population:
    print(p)
    

    
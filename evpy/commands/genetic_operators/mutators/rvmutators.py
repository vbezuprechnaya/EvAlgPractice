from random import random
from evpy.commands.genetic_operators.wrappers.command import Command


@Command
def real_valued_mutation(individual, n=None, m=10, h=10):
    if n == None: n = 1/len(individual)
    blinker = -1 if random() < .5 else 1
    alpha = .5 * h
    sigma = sum([pow(2, -x) for x in range(m) if random() <= (1/m)])
    for i in range(len(individual)):
        individual[i] = individual[i] + (blinker * alpha * sigma) if random() <= n else individual[i]
        
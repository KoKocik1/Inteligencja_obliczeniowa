import random
import numpy as np
import math


class EvolutionAlgorithm:

    def __init__(self):
        self.function = self.rotated_hyper_ellipsoid
        self.range = [-65.536, 65.536]
        self.expected_value = 0
        self.expected_range = [0, 0]

    def target_function(self, x):
        return self.function(x)

    def rotated_hyper_ellipsoid(self, x):
        return sum([(sum(x[:i+1]))**2 for i in range(len(x))])

    def styblinski_tang_function(self, x):
        return 0.5 * sum([(i**4 - 16*i**2 + 5*i) for i in x])

    def michalewicz_function(self, x, m=10):
        return -sum([math.sin(x[i]) * math.sin((i+1) * x[i]**2 / math.pi)**(2*m) for i in range(len(x))])

    def power_sum_function(self, x, p=4):
        return sum([abs(x[i])**(p+i) for i in range(len(x))])

    # def schwefel_function(self, x):
     #   return 418.9829 * len(x) - sum([x[i] * math.sin(math.sqrt(abs(x[i]))) for i in range(len(x))])

    def rastrigin_function(self, x):
        return 10 * len(x) + sum([(i**2 - 10 * math.cos(2 * math.pi * i)) for i in x])

    def ackley_function(self, x):
        a = 20
        b = 0.2
        c = 2 * math.pi
        n = len(x)
        sum1 = sum([i**2 for i in x])
        sum2 = sum([math.cos(c * i) for i in x])
        term1 = -a * math.exp(-b * math.sqrt(sum1 / n))
        term2 = -math.exp(sum2 / n)
        return term1 + term2 + a + math.e

    def schwefel_function(self, x):
        return 418.9829 * len(x) - sum([i * math.sin(math.sqrt(abs(i))) for i in x])

    # init with random individuals

    def init_population(self, size_of_population, dimension):
        # - dimension: count of features in one individual

        # Return:
        # - populacja: list of randomly generated individuals

        population = []

        for _ in range(size_of_population):

            # Generating an individual consisting of random values
            # in the range specified by self.range for each feature
            indyvidual = [random.uniform(self.range[0], self.range[1])
                          for _ in range(dimension)]

            population.append(indyvidual)

        return population

    def differential_mutation(self, poopulation, f):

        # Params:
        # - f: mutation coefficient, determining the strength of the mutation (0.7 given)

        # Return:
        # - new population with individuals subjected to mutation

        new_population = []

        for i in range(len(poopulation)):

            # random 3 indyviduals
            a, b, c = random.sample(poopulation, 3)

            # Differential mutation formula
            osobnik_mut = [a[j] + f * (b[j] - c[j]) for j in range(len(a))]
            new_population.append(osobnik_mut)

        return new_population

    # cross between parent and mutant

    def crossing_indyviduals(self, parent, mutant, cr):

        # Params:
        # - parent: individual from the population
        # - mutant: individual after mutation
        # - cr: crossover coefficient, determining the chance of choosing a value from the mutant individual

        # Return:
        # - child: nowy osobnik powstały w wyniku krzyżowania

        child = []

        for i in range(len(parent)):

            if random.random() < cr:

                child.append(mutant[i])
            else:
                child.append(parent[i])

        return child

    # Greedy succession: Method of selecting a new population based on the value of the objective function

    def greedy_succession(self, population, new_population):

        new_population.extend(population)

        # Sorting the population by the value of the objective function for each individual
        new_population.sort(key=lambda x: self.target_function(x))

        # Choosing the best individuals to create a new population based on the value of the objective function
        return new_population[:len(population)]

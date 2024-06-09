from algorithms.evolution_algorithm import EvolutionAlgorithm
from charts.charts import Charts
import numpy as np
import math

number_of_iterations = 10000
number_of_indeviduals = 100
f = 0.7
cr = 0.5
dimension = 3

algorithmNr = 4

points = np.random.rand(100, 3) * 100  # Losowe punkty 3D


evolutionAlgorithm = EvolutionAlgorithm()

if algorithmNr <= 1:
    evolutionAlgorithm.function = evolutionAlgorithm.rotated_hyper_ellipsoid
    evolutionAlgorithm.range = [-65.536, 65.536]
    evolutionAlgorithm.expected_value = 0
    evolutionAlgorithm.expected_range = [0, 0]

if algorithmNr == 2:
    evolutionAlgorithm.function = evolutionAlgorithm.power_sum_function
    evolutionAlgorithm.range = [0, dimension]
    evolutionAlgorithm.expected_value = 0
    evolutionAlgorithm.expected_range = [0, 0]

if algorithmNr == 3:
    evolutionAlgorithm.function = evolutionAlgorithm.styblinski_tang_function
    evolutionAlgorithm.range = [-5, 5]
    evolutionAlgorithm.expected_value = -39.16599*dimension
    evolutionAlgorithm.expected_range = [-2.903534, 2.903534]

if algorithmNr == 4:
    evolutionAlgorithm.function = evolutionAlgorithm.michalewicz_function
    evolutionAlgorithm.range = [0, math.pi]
    evolutionAlgorithm.expected_value = [-1.80, -2.76, -
                                         3.7, -4.69, -5.69, -6.68, -7.66, -8.66, -9.66, -10.65]
    evolutionAlgorithm.expected_range = [0, 0]

if algorithmNr >= 5:
    evolutionAlgorithm.funkcja = evolutionAlgorithm.schwefel_function
    evolutionAlgorithm.range = [-500, 500]
    evolutionAlgorithm.expected_value = 0
    evolutionAlgorithm.expected_range = [420.9687, 420.9687]

charts = Charts()

# population init
population = evolutionAlgorithm.init_population(
    number_of_indeviduals, dimension)

# points of charts x axis
points_of_charts = [1, 2, 5, 10, 15, 20, 50, 100, 500, 999]
axis_x = list(range(number_of_iterations))

best_solution_of_iteration = []
midium_solution_of_iteration = []
worst_solution_of_iteration = []

# main for - differential evolution
for iteration in range(number_of_iterations):
    new_population = evolutionAlgorithm.differential_mutation(population, f)
    for i in range(len(population)):
        new_population[i] = evolutionAlgorithm.crossing_indyviduals(
            population[i], new_population[i], cr)
    population = evolutionAlgorithm.greedy_succession(
        population, new_population)

    if dimension == 3:
        if iteration in points_of_charts:
            charts.generate_chart(
                f"Chart_iteration_{iteration}", np.array(population), evolutionAlgorithm.function, evolutionAlgorithm.range, evolutionAlgorithm.range)

    # values of function for each individual
    values_of_function = [evolutionAlgorithm.target_function(
        osobnik) for osobnik in population]

    # best, midium and worst solution in iteration
    best_value = min(values_of_function)
    midium_value = np.mean(values_of_function)
    worst_value = max(values_of_function)

    best_solution_of_iteration.append(best_value)
    midium_solution_of_iteration.append(midium_value)
    worst_solution_of_iteration.append(worst_value)

best_solution = min(
    population, key=lambda x: evolutionAlgorithm.target_function(x))
best_value_global = evolutionAlgorithm.target_function(best_solution)
print("Best solution:", best_solution)
print("Value of funciton for best solution:", best_value_global)
print("Expected value:", evolutionAlgorithm.expected_value)
print(f"Expected range: {evolutionAlgorithm.expected_range}")

charts.display_charts()

charts.generate_final_chart(
    best_solution_of_iteration, midium_solution_of_iteration, worst_solution_of_iteration, axis_x)

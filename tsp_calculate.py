import random
import math
import matplotlib.pyplot as plt
import os
folderName = "tsp_img"


def plot_route(route, cities, title):
    plt.figure(figsize=(10, 6))
    x = [cities[city][0] for city in route] + [cities[route[0]][0]]
    y = [cities[city][1] for city in route] + [cities[route[0]][1]]
    plt.plot(x, y, marker='o')
    plt.title(title)
    plt.savefig(f"{folderName}/{title}.png")
    plt.close()

# distance between two cities


def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# total distance of the route


def total_distance(route, cities):
    total = 0
    for i in range(len(route) - 1):
        total += calculate_distance(cities[route[i]], cities[route[i+1]])

    # Add distance to the first city
    total += calculate_distance(cities[route[-1]], cities[route[0]])
    return total

# generate a random route


def generate_random_route(cities):
    return random.sample(range(len(cities)), len(cities))

# swap two random cities in the route


def swap(route):
    idx1, idx2 = random.sample(range(len(route)), 2)
    route[idx1], route[idx2] = route[idx2], route[idx1]
    return route

# swap the order of a random subroute


def reverse_subroute(route):
    start, end = sorted(random.sample(range(len(route)), 2))
    route[start:end+1] = reversed(route[start:end+1])
    return route

# random subroute shuffle


def shuffle(route):
    start, end = sorted(random.sample(range(len(route)), 2))
    shuffled_segment = route[start:end+1]
    random.shuffle(shuffled_segment)
    route[start:end+1] = shuffled_segment
    return route

# random insert city to another position


def random_insert(route):
    idx1, idx2 = random.sample(range(len(route)), 2)
    route.insert(idx1, route.pop(idx2))
    return route


def simulated_annealing(cities, initial_temperature=100000, cooling_rate=0.99999, stopping_temperature=0.00001, log_interval=100000, plot_interval=100000):
    # def simulated_annealing(cities, initial_temperature=1000, cooling_rate=0.99999, stopping_temperature=0.0001, log_interval=100000, plot_interval=100000):
    current_solution = generate_random_route(cities)
    current_distance = total_distance(current_solution, cities)
    best_solution = current_solution.copy()
    best_distance = current_distance

    temperature = initial_temperature
    iteration = 0
    distances = []

    while temperature > stopping_temperature:
        operator = random.choice(
            [swap, reverse_subroute, shuffle, random_insert])
        new_solution = operator(current_solution.copy())
        new_distance = total_distance(new_solution, cities)

        if new_distance < current_distance or random.random() < math.exp((current_distance - new_distance) / temperature):
            current_solution = new_solution
            current_distance = new_distance

        if current_distance < best_distance:
            best_solution = current_solution.copy()
            best_distance = current_distance

        if iteration % log_interval == 0:
            distances.append(best_distance)

        if iteration % plot_interval == 0:
            plot_route(best_solution, cities,
                       f'Best Route at Iteration {iteration}')
            # if (iteration == 1000000):
            #     plot_interval = 10000000

        temperature *= cooling_rate
        iteration += 1

    distances.append(best_distance)
    plot_route(best_solution, cities, 'Final Best Route')

    return best_solution, best_distance, distances


def read_tsplib(file_path):
    cities = []
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            if line.startswith("NODE_COORD_SECTION"):
                break
        for line in lines:
            if line.startswith("EOF"):
                break
            parts = line.split()
            if len(parts) == 3:
                try:
                    cities.append((float(parts[1]), float(parts[2])))
                except ValueError:
                    print("Error parsing coordinates in line:", line)
    return cities


# from git
# tsplib_files = ["tsp_small/berlin52.tsp", "tsp_small/eil51.tsp",
#                "tsp_small/st70.tsp", "tsp_small/eil76.tsp", "tsp_small/eil101.tsp"]
# tsplib_files = ["tsp_large/a280.tsp", "tsp_large/brd14051.tsp",
#                 "tsp_large/dsj1000.tsp", "tsp_large/gr666.tsp", "tsp_large/pr1002.tsp"]
tsplib_files = ["tsp_large/brd14051.tsp"]

for file_name in tsplib_files:
    file_path = file_name
    folderName = "tsp_img/"+file_name.split("/")[1]
    if not os.path.exists(folderName):
        os.makedirs(folderName)
    cities = read_tsplib(file_path)
    best_solution, best_distance, distances = simulated_annealing(cities)
    plt.plot(distances)
    plt.xlabel('Iteration (x100)')
    plt.ylabel('Best Distance')
    plt.title('Best Distance over Iterations for '+file_name)
    plt.xticks(range(len(distances)), [str(i*100)
               for i in range(len(distances))])
    # plt.show()
    plt.savefig(f'{folderName}/results.png')
    plt.close()
    print("File:", file_name)
    print("Best Route:", best_solution)
    print("Best Distance:", best_distance)
    print("------------------------")

import random
import math

import random
import math

# Funkcja obliczająca długość trasy
def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Funkcja obliczająca długość całej trasy
def total_distance(route, cities):
    total = 0
    for i in range(len(route) - 1):
        total += calculate_distance(cities[route[i]], cities[route[i+1]])
    total += calculate_distance(cities[route[-1]], cities[route[0]])  # Dodanie dystansu do pierwszego miasta
    return total

# Funkcja generująca losową trasę
def generate_random_route(cities):
    return random.sample(range(len(cities)), len(cities))

# Operator zamieniający dwa losowe miasta w trasie
def swap(route):
    idx1, idx2 = random.sample(range(len(route)), 2)
    route[idx1], route[idx2] = route[idx2], route[idx1]
    return route

# Operator odwracający kolejność fragmentu trasy
def reverse_subroute(route):
    start, end = sorted(random.sample(range(len(route)), 2))
    route[start:end+1] = reversed(route[start:end+1])
    return route

# Operator przemieszczający losowy podciąg trasy na inne miejsce
def shuffle(route):
    start, end = sorted(random.sample(range(len(route)), 2))
    shuffled_segment = route[start:end+1]
    random.shuffle(shuffled_segment)
    route[start:end+1] = shuffled_segment
    return route

# Operator losowo wstawiający miasto w inną pozycję
def random_insert(route):
    idx1, idx2 = random.sample(range(len(route)), 2)
    route.insert(idx1, route.pop(idx2))
    return route

# Funkcja wykorzystująca algorytm symulowanego wyżarzania
def simulated_annealing(cities, initial_temperature=1000, cooling_rate=0.99, stopping_temperature=0.1):
    current_solution = generate_random_route(cities)
    current_distance = total_distance(current_solution, cities)
    best_solution = current_solution.copy()
    best_distance = current_distance

    temperature = initial_temperature
    while temperature > stopping_temperature:
        # Losowy wybór jednego z czterech operatorów
        operator = random.choice([swap, reverse_subroute, shuffle, random_insert])
        new_solution = operator(current_solution.copy())
        new_distance = total_distance(new_solution, cities)
        
        # Akceptacja gorszego rozwiązania z pewnym prawdopodobieństwem
        if new_distance < current_distance or random.random() < math.exp((current_distance - new_distance) / temperature):
            current_solution = new_solution
            current_distance = new_distance
        
        # Aktualizacja najlepszego rozwiązania
        if current_distance < best_distance:
            best_solution = current_solution.copy()
            best_distance = current_distance
        
        # Schładzanie
        temperature *= cooling_rate
    
    return best_solution, best_distance


# Funkcja wczytująca dane z pliku TSPLib
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

# Lista plików z zestawami TSPLib
tsplib_files = ["tsp/berlin52.tsp", "tsp/eil51.tsp", "tsp/st70.tsp", "tsp/eil76.tsp", "tsp/eil101.tsp"]

# Wywołanie algorytmu symulowanego wyżarzania dla każdego zestawu danych
for file_name in tsplib_files:
    file_path = file_name  # Wstaw ścieżkę do katalogu z plikami TSPLib
    cities = read_tsplib(file_path)
    best_route, best_distance = simulated_annealing(cities)
    print("File:", file_name)
    print("Best Route:", best_route)
    print("Best Distance:", best_distance)
    print("------------------------")
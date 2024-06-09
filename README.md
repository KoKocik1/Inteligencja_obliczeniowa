# find_minimum_and_tsp_calculate

This repository contains two Python programs:

1. **find_minimum**: Calculates the minimum of various high-dimensional functions (from 2 to 50 dimensions) using an evolutionary algorithm.
2. **tsp_calculate**: Finds the shortest path for the Traveling Salesman Problem (TSP) and visualizes the solution during the computation.

## find_minimum

This program is designed to find the minimum of several well-known mathematical functions in dimensions ranging from 2 to 50. The functions implemented are:

- **Rotated Hyper-Ellipsoid Function**
- **Styblinski-Tang Function**
- **Michalewicz Function**
- **Power Sum Function**
- **Schwefel Function**

### Functions Implemented

````python
def rotated_hyper_ellipsoid(self, x):
    return sum([(sum(x[:i+1]))**2 for i in range(len(x))])

def styblinski_tang_function(self, x):
    return 0.5 * sum([(i**4 - 16*i**2 + 5*i) for i in x])

def michalewicz_function(self, x, m=10):
    return -sum([math.sin(x[i]) * math.sin((i+1) * x[i]**2 / math.pi)**(2*m) for i in range(len(x))])

def power_sum_function(self, x, p=4):
    return sum([abs(x[i])**(p+i) for i in range(len(x))])

def schwefel_function(self, x):
    return 418.9829 * len(x) - sum([x[i] * math.sin(math.sqrt(abs(x[i]))) for i in range(len(x))])


### Visualization

The `find_minimum` program also plots the convergence of the optimization process, showcasing:

- **Best solutions**: The optimal solutions found during the optimization process.
- **Worst solutions**: The least optimal solutions encountered.
- **Average solutions**: The average performance of the solutions over time.

### Usage

To use the `find_minimum` program, simply run the script. It utilizes an evolutionary algorithm to find the minimum of the chosen functions and displays the results graphically.

## tsp_calculate

This program solves the Traveling Salesman Problem (TSP) by finding the shortest possible route that visits each city exactly once and returns to the origin city. It also provides visualizations of the connections during the computation process.

### Visualization

The `tsp_calculate` program visualizes the path taken by the algorithm to find the shortest route, allowing users to see the progress of the solution in real-time. This includes:

- **Initial random path**: The initial random solution.
- **Intermediate paths**: Paths at various stages of the optimization.
- **Final optimal path**: The shortest path found by the algorithm.

### Usage

To use the `tsp_calculate` program, simply run the script. It will compute the shortest path for the given set of cities and display the results graphically.

## Installation

To run these programs, you need to have Python installed along with the necessary libraries. You can install the required libraries using the following command:

```bash
pip install -r requirements.txt

## Running the Programs

### find_minimum

```bash
python find_minimum.py

###tcp_calculate

```bash
python tsp_calculate.py

##Contributions
Contributions are welcome! Please feel free to submit a Pull Request.

##License
This project is licensed under the MIT License - see the LICENSE file for details.
````

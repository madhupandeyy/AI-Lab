import random
import math

def calculate_cost(state):
    cost = 0
    n = len(state)
    for i in range(n):
        for j in range(i + 1, n):
            if state[i] == state[j] or abs(state[i] - state[j]) == abs(i - j):
                cost += 1
    return cost

def get_neighbors(state):
    neighbors = []
    n = len(state)
    for col in range(n):
        for row in range(n):
            if state[col] != row:
                new_state = list(state)
                new_state[col] = row
                neighbors.append(new_state)
    return neighbors

def simulated_annealing(initial_state, schedule, max_iterations=1000):
    current_state = initial_state
    current_cost = calculate_cost(current_state)

    for t in range(max_iterations):
        T = schedule(t)
        if T == 0:
            break

        if current_cost == 0:
            return current_state

        neighbors = get_neighbors(current_state)
        next_state = random.choice(neighbors)
        next_cost = calculate_cost(next_state)

        ΔE = next_cost - current_cost

        if ΔE < 0 or random.random() < math.exp(-ΔE / T):
            current_state, current_cost = next_state, next_cost
            print(f"Iteration {t}: Current state: {current_state}, Cost: {current_cost}, T: {T}")

    print(f"Max iterations reached without finding a solution.")
    return None

def linear_schedule(t, initial_temp=1000, final_temp=1, max_iter=1000):
    return max(final_temp, initial_temp - (initial_temp - final_temp) * (t / max_iter))

try:
    n = int(input("Enter the number of queens (N): "))
    if n <= 0:
        raise ValueError("N must be a positive integer.")

    initial_state = list(map(int, input(f"Enter the initial state as a list of {n} integers (rows for each column): ").split()))
    if len(initial_state) != n or any(not (0 <= row < n) for row in initial_state):
        raise ValueError(f"Invalid initial state. Please provide {n} integers between 0 and {n-1}.")
except ValueError as e:
    print(e)
    n = 4
    initial_state = [random.randint(0, n - 1) for _ in range(n)]
    print(f"Using random initial state: {initial_state}")

solution = None

while solution is None:
    solution = simulated_annealing(initial_state, linear_schedule)

print(f"Solution found: {solution}")

#Assignment 3 - Luke Julien Biber
import numpy as np

### 1. Simulate Daily Demand and Analyze Results
def daily_demand(n):
    np.random.seed(0)
    daily_demand = np.random.poisson(lam=20, size=n)
    return daily_demand

def analyze_demand(demand):
    print(f"Mean daily demand: {np.mean(demand):.2f}")
    print(f"Standard deviation: {np.std(demand):.2f}")
    print(f"5th percentile: {np.percentile(demand, 5):.2f}")
    print(f"95th percentile: {np.percentile(demand, 95):.2f}")

#Task 1
days = 30
daily = daily_demand(days)
print(f"One month daily demand: {daily}")
analyze = analyze_demand(daily)
# Interpretation:
    # The results show that the daily demand centers around 20 units, with moderate variability (±4 units).
    # The 5th percentile (14.45) suggests that on particularly low-demand days, we might see around 14 units sold.
    # The 95th percentile (27.20) indicates that on high-demand days, sales could reach up to approximately 27 units.

### 2. Inventory Level Simulation
def demand_simulation(n):
    np.random.seed(0)
    monthly_demand = np.random.poisson(lam=20, size=(n, 30)).sum(axis=1)
    return monthly_demand

def optimal_inventory_level(simulations):
    optimal = np.percentile(simulations, 95)
    return optimal

#Task 2
simulations = demand_simulation(1000)
optimal = optimal_inventory_level(simulations)
print(f"The optimal monthly inventory level is: {optimal}")

### 3. Optional
#To further enhance your simulation, consider the following improvement:
#- Create a user interface to input different assumptions (e.g., average daily demand, service level).



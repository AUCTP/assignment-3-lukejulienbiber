# Assignment 3 - Luke Julien Biber
import numpy as np

### 1. Simulate Daily Demand and Analyze Results
def daily_demand(lam, days):
    np.random.seed(0)
    return np.random.poisson(lam=lam, size=days)

def analyze_demand(demand):
    print(f"\n--- Daily Demand Analysis ---")
    print(f"Mean daily demand: {np.mean(demand):.2f}")
    print(f"Standard deviation: {np.std(demand):.2f}")
    print(f"5th percentile: {np.percentile(demand, 5):.2f}")
    print(f"95th percentile: {np.percentile(demand, 95):.2f}")

### 2. Inventory Level Simulation
def demand_simulation(n_simulations, lam, days):
    np.random.seed(0)
    simulated_total_demand = np.random.poisson(lam=lam, size=(n_simulations, days)).sum(axis=1)
    return simulated_total_demand

def optimal_inventory_level(simulations, service_level_percent):
    return np.percentile(simulations, service_level_percent)

### 3. User Input
def user_interface():
    print("--- Welcome to the Inventory Management System ---")
    lam = float(input("Enter the average daily demand (lambda): "))
    service_level = float(input("Enter the desired service level (e.g. 95 for 95%): "))
    days = int(input("Enter the number of days for inventory planning: "))
    return lam, service_level, days

### Main Program
lam, service_level, days = user_interface()

# Task 1: Daily Demand Simulation & Analysis
daily = daily_demand(lam, days)
analyze_demand(daily)

# Task 2: Monte Carlo Simulation for Inventory Level
simulations = demand_simulation(1000, lam, days)
optimal = optimal_inventory_level(simulations, service_level)

print(f"\n--- Inventory Recommendation ---")
print(f"The optimal inventory level for {days} days is: {optimal:.2f}")
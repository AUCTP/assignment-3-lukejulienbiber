#Assignment 3 - Luke Julien Biber
import numpy as np

### 1. Simulate Daily Demand and Analyze Results
def daily_demand(lam):
    np.random.seed(0)
    daily_demand = np.random.poisson(lam=lam, size=30)
    return daily_demand

def analyze_demand(demand):
    print(f"Mean daily demand: {np.mean(demand):.2f}")
    print(f"Standard deviation: {np.std(demand):.2f}")
    print(f"5th percentile: {np.percentile(demand, 5):.2f}")
    print(f"95th percentile: {np.percentile(demand, 95):.2f}")

### 2. Inventory Level Simulation
def demand_simulation(n, lam):
    np.random.seed(0)
    monthly_demand = np.random.poisson(lam=lam, size=(n, 30)).sum(axis=1)
    return monthly_demand

def optimal_inventory_level(simulations, service_level):
    optimal = np.percentile(simulations, service_level)
    return optimal

### 3. Optional
def user_interface():
    print("Welcome to the Inventory Management System")
    lam = float(input("Enter the average daily demand (lambda): "))
    service_level = float(input("Enter the desired service level (percentile e.g 95 for 95%): "))
    return lam, service_level

#Main Program
lam, service_level= user_interface()
daily = daily_demand(lam)
analyze_demand(daily)
simulations = demand_simulation(1000, lam)
optimal = optimal_inventory_level(simulations, service_level)
print(f"The optimal monthly inventory level is: {optimal}")

# Interpretation:
    # The results show that the daily demand centers around 20 units, with moderate variability (±4 units).
    # The 5th percentile (14.45) suggests that on particularly low-demand days, we might see around 14 units sold.
    # The 95th percentile (27.20) indicates that on high-demand days, sales could reach up to approximately 27 units.
    # The optimal inventory level is 642.05
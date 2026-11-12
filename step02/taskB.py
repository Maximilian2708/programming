# Name: Maximilian Kirsh
# Date: 2026-11-11
# Program: Road trip calculator
# Description: figures out gas costs per person, and driving time

average_speed = 55

destination = input("Destination: ")
trip_distance = input("Trip distance: ")
distance = int(trip_distance)
mile_per_gallon = input("Cars mpg: ")
car_mpg = int(mile_per_gallon)
gas_price = input("Gas price: ")
gas = float(gas_price)
people_splitting = input("Number of people splitting the cost: ")
print()
people = int(people_splitting)
print("-" *3 +"Trip to Columbus" + "-" *3)
gallons_of_gas = distance / car_mpg
print("Gallons of gas: ", gallons_of_gas)
gas_cost = gallons_of_gas * gas
print("Gas cost: ", gas_cost)
cost_per_person = gas_cost / people
print("Cost per person: ", cost_per_person)
driving_time_minutes = distance / average_speed *60
minutes = int(driving_time_minutes)
driving_time_hours = driving_time_minutes // 60
hours = int(driving_time_hours)
leftover_minutes = driving_time_minutes % 60
leftover = int(leftover_minutes)
print("Driving time: ", hours, leftover)
round_trip = gas_cost *2
print("Round trip gas: ", round_trip)

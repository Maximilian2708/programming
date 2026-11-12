# Name: Maximilian Kirsh
# Date: 2026-11-10
# Program: Pizza Party Planner
# Description: Plans pizza for a party: how many pizzas, how many slices, cost

slices_per_pizza = 8
pizza_price = 12.99
slice_price = 2.25

host_name = input("Host Name: ")
number_of_people = input("Number of people: ")
people = int(number_of_people)
slices_per_person = input("Slices per person: ")
slices = int(slices_per_person)
print()
print("=" *3 + "Pizza Plan for Max's Party" + "=" *3)
slices_needed = people * slices
print("Slices needed: ", slices_needed)
whole_pizzas = slices_needed // slices_per_pizza
print("Whole pizzas: ", whole_pizzas)
extra_slices = slices_needed % slices_per_pizza
print("Extra slices: ", extra_slices)
total_cost = whole_pizzas * pizza_price + extra_slices * slice_price
print("Total cost: ", total_cost)
cost_per_person = total_cost / people
print("Cost per person: ", cost_per_person)

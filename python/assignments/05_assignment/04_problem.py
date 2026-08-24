import json

cities = {
    "Delhi": 32900000,
    "Mumbai": 21600000,
    "Bangalore": 14000000
}

with open("assignments/05_assignment/citis.json", "w") as f:
    json.dump(cities, f, indent=4)


with open("assignments/05_assignment/citis.json", "r") as f:
    data = json.load(f)
    
print("Cities and their population: ")
for city, population in data.items():
    print(city, ":" , population)


new_city = input("enter new city: ")
new_population = int(input("enter new population: "))

cities[new_city] = new_population

with open("assignments/05_assignment/citis.json", "w") as f:
    json.dump(cities, f, indent=4)

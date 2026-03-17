# =========================
# Q3. Perform operations on city.txt
# a) Display all cities
# b) Cities with population > 10 lakhs
# c) Sum of areas
# =========================

cities = []

with open("city.txt", "r") as f:
    for line in f:
        name, pop, area = line.split()
        cities.append((name, float(pop), float(area)))

# a)
print("\nAll cities:")
for c in cities:
    print(c)

# b)
print("\nCities with population > 10 lakhs:")
for c in cities:
    if c[1] > 10:
        print(c[0])

# c)
total_area = sum(c[2] for c in cities)
print("\nTotal area:", total_area)

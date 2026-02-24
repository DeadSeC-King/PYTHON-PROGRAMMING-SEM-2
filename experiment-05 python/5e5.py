# 5. Store details of n movies in a dictionary.
# Each movie: name, year, director, production cost, collection
# a) print all movie details
# b) display movies released before 2015
# c) print movies that made profit
# d) print movies by particular director

n = int(input("Enter number of movies: "))
movies = {}

for i in range(n):
    name = input("Movie name: ")
    year = int(input("Year: "))
    director = input("Director: ")
    cost = float(input("Production cost: "))
    collection = float(input("Collection: "))
    
    movies[name] = {
        "year": year,
        "director": director,
        "cost": cost,
        "collection": collection
    }

print("All movie details:")
for m, d in movies.items():
    print(m, d)

print("Movies before 2015:")
for m, d in movies.items():
    if d["year"] < 2015:
        print(m)

print("Profitable movies:")
for m, d in movies.items():
    if d["collection"] > d["cost"]:
        print(m)

search_dir = input("Enter director name to search: ")
print("Movies by", search_dir)
for m, d in movies.items():
    if d["director"].lower() == search_dir.lower():
        print(m)

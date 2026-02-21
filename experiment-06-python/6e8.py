data = {"a": 10, "b": 10, "c": 10}

all_same = lambda d: len(set(d.values())) == 1

print(all_same(data))
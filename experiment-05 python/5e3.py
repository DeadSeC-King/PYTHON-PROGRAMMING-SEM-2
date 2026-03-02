n = int(input("Enter number of students: "))
scores = list(map(int, input("Enter scores: ").split()))

first = second = float('-inf')

for s in scores:
    if s > first:
        second = first
        first = s
    elif s > second and s != first:
        second = s

if second == float('-inf'):
    print("No runner-up score exists")
else:
    print("Runner-up score:", second)
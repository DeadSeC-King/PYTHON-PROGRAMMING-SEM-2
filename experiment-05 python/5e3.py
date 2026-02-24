
# 3. WAP to input a list of scores for N students. Find the runner-up score.

n = int(input("Enter number of students: "))
scores = list(map(int, input("Enter scores: ").split()))

unique_scores = list(set(scores))
unique_scores.sort(reverse=True)

runner_up = unique_scores[1]
print("Runner-up score:", runner_up)

scores = [88, 92, 76, 81, 95, 89, 77, 85, 91, 87]
import statistics
mean_score = statistics.mean(scores)
median_score = statistics.median(scores)
mode_score = statistics.mode(scores)
std_dev = statistics.stdev(scores)
variance = statistics.variance(scores)
print(f"Mean: {mean_score}")
print(f"Median: {median_score}")
print(f"Mode: {mode_score}")
print(f"Standard Deviation: {std_dev}")
print(f"Variance: {variance}")
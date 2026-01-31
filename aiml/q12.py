import csv

# csv file for panda experiments with 500 values
header = ["Name","cgpa"]
rows = [
    ["Krran", 8.5],
    ["Rahul", 8.2],
    ["Aman", 7.9],
    ["Sakshi", 8.7],
    ["Anjali", 8.0],
    ["Rohan", 7.5]
]

# Create and write to CSV file
with open("students.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(header)   # write header
    writer.writerows(rows)    # write data

print("CSV file created successfully.")

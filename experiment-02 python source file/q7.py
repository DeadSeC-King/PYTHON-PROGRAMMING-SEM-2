#wap to print th egrade sheet of studnet for the given range of cgpa. scan five marks subjects and calculate the percentage .abs
#cgpa=percentage/10
"""cgpa range
    0-3.4>F
    3.5-5.0 >C+
    5.1-6>B
    6.1-7>B+
    7.1-8>a
    8.1-9>A+
    9.1-10>o
"""
def calculate_grade(percentage):
    cgpa = percentage / 10
    if 0 <= cgpa <= 3.4:
        return 'F'
    elif 3.5 <= cgpa <= 5.0:
        return 'C+'
    elif 5.1 <= cgpa <= 6.0:
        return 'B'
    elif 6.1 <= cgpa <= 7.0:
        return 'B+'
    elif 7.1 <= cgpa <= 8.0:
        return 'A'
    elif 8.1 <= cgpa <= 9.0:
        return 'A+'
    elif 9.1 <= cgpa <= 10.0:
        return 'O'
    else:
        return 'Invalid CGPA'
def main():
    marks = []
    for i in range(5):
        mark = float(input(f"Enter marks for subject {i+1}: "))
        marks.append(mark)
    total_marks = sum(marks)
    percentage = (total_marks / 500) * 100
    grade = calculate_grade(percentage)
    print(f"Total Marks: {total_marks}")
    print(f"Percentage: {percentage:.2f}%")
    print(f"Grade: {grade}")
if __name__ == "__main__":
    main()



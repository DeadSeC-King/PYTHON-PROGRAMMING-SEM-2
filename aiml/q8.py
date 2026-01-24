import random
import statistics
students = [
    "Aarav","Aaryan","Aditya","Akash","Aman","Amit","Aniket","Animesh","Ankit","Anmol","Arjun","Aryan","Ayush","Bhavesh","Chirag",
    "Dev","Dhruv","Gaurav","Harsh","Ishaan","Karan","Kartik","Ketan","Kunal","Kush","Manish","Mohit","Naman","Nikhil","Pankaj",
    "Pranav","Rahul","Raj","Rajat","Ravi","Rohit","Rohan","Sachin","Sagar","Sahil","Sandeep","Sanjay","Shivam","Shubham","Siddharth",
    "Sumit","Suraj","Tanishq","Uday","Varun","Aanchal","Aditi","Alka","Anamika","Ananya","Anjali","Ankita","Aparna","Archana","Bhavya",
    "Deepika","Divya","Isha","Kajal","Kavya","Khushi","Komal","Megha","Neha","Nikita","Pooja","Priya","Radhika","Ritu","Riya","Sakshi",
    "Shalini","Shivani","Shruti","Sneha","Sonali","Suman","Swati","Tanvi","Trisha","Vaishali","Vandana","Yashika","Zoya","Kritika"
]
marks = [random.randint(0, 100) for _ in students]
meanmarks=statistics.mean(marks) ;medianmarks=statistics.median(marks)
modemarks=statistics.mode(marks) ;variance=statistics.variance(marks)
stddevmarks=statistics.stdev(marks) ;iqr=marks[74]-marks[24]
q1=marks[24] ;q2=marks[49] ;q3=marks[74]
lowerlimit=q1-1.5*iqr ;upperlimit=q3+1.5*iqr
print("iqr is",iqr) ;print("q1 is",q1)
print("q2 is",q2) ;print("q3 is",q3)
student_marks = dict(zip(students, marks))
print("the upper limit is ",upperlimit) ;print("the lower limit is",lowerlimit)
sorted_students = sorted(student_marks.items(), key=lambda x: x[1])
filtered_students = {
    student: mark
    for student, mark in student_marks.items()
    if lowerlimit <= mark <= upperlimit}
print(filtered_students)
filtered_marks = list(filtered_students.values())
mean_val = statistics.mean(filtered_marks)
median_val = statistics.median(filtered_marks)
mode_val = statistics.mode(filtered_marks)
variance_val = statistics.variance(filtered_marks)
std_dev_val = statistics.stdev(filtered_marks)
print("After filtration new statistical data is") ;print("Mean:", mean_val)
print("Median:", median_val) ;print("Mode:", mode_val)
print("Variance:", variance_val) ;print("Standard Deviation:", std_dev_val)
grade_points = {'A+': 4.0, 'A': 4.0, 'A-': 3.7, 'B+': 3.3, 'B': 3.0, 'B-': 2.7, 'C+': 2.3, 'C': 2.0, 'C-': 1.7, 'D+': 1.3, 'D': 1.0, 'D-': 0.7, 'F': 0.0}

total_points = 0
count = 0

while True:
    grade = input("Enter a letter grade: ")
    
    if grade == "":
        break
    
    if grade in grade_points:
        total_points += grade_points[grade]
        count += 1

if count > 0:
    gpa = total_points / count
    print("Grade Point Average:", gpa)
else:
    print("No grades entered.")

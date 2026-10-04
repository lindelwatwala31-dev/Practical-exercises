marks_obtained = float(input("Enter marks obtained: "))
total_marks = float(input("Enter total marks: "))
grade_perc = (marks_obtained / total_marks) * 100
if grade_perc >= 75:
    print("Distinction")
elif grade_perc >= 74 and grade_perc >= 60:
    print("Merit")
elif grade_perc <= 59 and grade_perc >= 50:
    print("Pass")
else:
    print("Fail")


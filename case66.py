
# Case 66: Student Academic Risk Classification

name = input("Enter student name: ")

marks = []

for i in range(5):
    mark = float(input("Enter subject " + str(i + 1) + " marks: "))
    marks.append(mark)

attendance = float(input("Enter attendance percentage: "))

average = sum(marks) / len(marks)

if average < 40 or attendance < 60:
    risk = "High Risk"
elif average < 60 or attendance < 75:
    risk = "Medium Risk"
else:
    risk = "Low Risk"

print("\n--- Academic Risk Report ---")
print("Student:", name)
print("Marks:", marks)
print("Average:", average)
print("Attendance:", attendance, "%")
print("Academic Risk:", risk)

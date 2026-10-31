
# Case 1: University Scholarship Allocation

name = input("Enter student name: ")
marks = []

for i in range(5):
    mark = float(input("Enter subject " + str(i + 1) + " marks: "))
    marks.append(mark)

attendance = float(input("Enter attendance percentage: "))
income = float(input("Enter annual family income: "))

aggregate = sum(marks) / len(marks)

print("\n--- Scholarship Report ---")
print("Student:", name)
print("Subject marks:", marks)
print("Aggregate:", aggregate)

if (aggregate >= 80 and min(marks) >= 70
        and attendance >= 75 and income <= 250000):
    print("Result: Eligible for scholarship")
else:
    print("Result: Not eligible for scholarship")


# Case 42: Student Marks Matrix Analysis

students = ["Student 1", "Student 2", "Student 3"]
subjects = ["Python", "Maths", "English"]

marks = []

for i in range(3):
    row = []
    print("\nEnter marks for", students[i])

    for j in range(3):
        mark = float(input("Enter " + subjects[j] + " marks: "))
        row.append(mark)

    marks.append(row)

totals = []

print("\n--- Student Marks Report ---")

for i in range(3):
    total = sum(marks[i])
    average = total / 3
    totals.append(total)

    print(students[i])
    print("Marks:", marks[i])
    print("Total:", total)
    print("Average:", average)

highest = max(totals)
position = totals.index(highest)

print("\nTop Performer:", students[position])
print("Highest Total:", highest)

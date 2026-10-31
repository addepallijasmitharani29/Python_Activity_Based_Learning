
# Case 100: Comprehensive Smart Campus Management Simulation

students = []

number = int(input("Enter number of students: "))

for i in range(number):
    print("\nEnter details for Student", i + 1)

    name = input("Student name: ")
    attendance = float(input("Attendance percentage: "))
    fee_paid = float(input("Fee amount paid: "))
    library_fine = float(input("Library fine: "))

    event_choice = input("Register for campus event? (yes/no): ")

    if attendance >= 75 and fee_paid >= 55000 and library_fine == 0:
        status = "Eligible"
    else:
        status = "Not Eligible"

    if event_choice.lower() == "yes":
        event_status = "Registered"
    else:
        event_status = "Not Registered"

    student = (name, attendance, fee_paid,
               library_fine, status, event_status)

    students.append(student)

print("\n--- SMART CAMPUS MANAGEMENT REPORT ---")

eligible_count = 0
registered_count = 0
total_fees = 0
total_fines = 0

for student in students:
    print("\nStudent:", student[0])
    print("Attendance:", student[1], "%")
    print("Fee Paid: Rs.", student[2])
    print("Library Fine: Rs.", student[3])
    print("Academic and Fee Status:", student[4])
    print("Event Status:", student[5])

    if student[4] == "Eligible":
        eligible_count += 1

    if student[5] == "Registered":
        registered_count += 1

    total_fees += student[2]
    total_fines += student[3]

print("\n--- CAMPUS SUMMARY ---")
print("Total Students:", len(students))
print("Eligible Students:", eligible_count)
print("Event Registrations:", registered_count)
print("Total Fees Collected: Rs.", total_fees)
print("Total Library Fines: Rs.", total_fines)

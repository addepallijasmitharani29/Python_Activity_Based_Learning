
# Case 71: Integrated University Fee and Eligibility Audit

name = input("Enter student name: ")

tuition_fee = 50000
library_fee = 2000
lab_fee = 3000

total_fee = tuition_fee + library_fee + lab_fee

paid = float(input("Enter amount paid: "))
attendance = float(input("Enter attendance percentage: "))

balance = total_fee - paid

print("\n--- University Audit Report ---")
print("Student:", name)
print("Total fee:", total_fee)
print("Amount paid:", paid)
print("Fee balance:", balance)

if paid >= 55000:
    fee_status = "Fee Eligible"
else:
    fee_status = "Fee Not Eligible"

if attendance >= 75:
    academic_status = "Academically Eligible"
else:
    academic_status = "Academically Not Eligible"

print("Fee Status:", fee_status)
print("Academic Status:", academic_status)

if fee_status == "Fee Eligible" and academic_status == "Academically Eligible":
    print("Final Result: Eligible")
else:
    print("Final Result: Not Eligible")

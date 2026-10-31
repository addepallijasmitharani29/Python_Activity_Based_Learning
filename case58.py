
# Case 58: Library Borrowing and Fine Reconciliation

borrowers = []
fines = []

number = int(input("Enter number of borrowers: "))

for i in range(number):
    name = input("\nEnter borrower name: ")
    days = int(input("Enter number of borrowing days: "))

    if days < 0:
        print("Invalid number of days")
        continue

    if days > 7:
        fine = (days - 7) * 5
    else:
        fine = 0

    borrowers.append((name, days))
    fines.append(fine)

    print("Borrower:", name)
    print("Borrowing days:", days)
    print("Fine: Rs.", fine)

print("\n--- Library Fine Report ---")

for i in range(len(borrowers)):
    print(borrowers[i][0], "Fine: Rs.", fines[i])

print("Total fine collected: Rs.", sum(fines))

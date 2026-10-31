
# Case 13: ATM Transaction Sequence Simulation

balance = 10000
transactions = []

while True:
    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        amount = float(input("Enter deposit amount: "))

        if amount > 0:
            balance += amount
            transactions.append(("Deposit", amount))
            print("Deposit successful")
        else:
            print("Enter a valid amount")

    elif choice == 2:
        amount = float(input("Enter withdrawal amount: "))

        if amount <= 0:
            print("Enter a valid amount")
        elif amount <= balance:
            balance -= amount
            transactions.append(("Withdrawal", amount))
            print("Withdrawal successful")
        else:
            print("Insufficient balance")

    elif choice == 3:
        print("Current balance:", balance)

    elif choice == 4:
        break

    else:
        print("Invalid choice")

print("\n--- Transaction History ---")
for transaction in transactions:
    print(transaction[0], ":", transaction[1])

print("Final balance:", balance)

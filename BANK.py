accounts={"101":1000, "102":2000, "103":3000}
while True:
    print("1. DEPOSIT")
    print("2. WITHDRAW")
    print("3. TRANSFER")
    print("4. BALANCE")
    print("5. LOGOUT")
    ch = int(input("Enter your choice:"))
    if ch == 1:
        acc = input("enter the acc number: ")
        amt = int(input("Enter the amount to deposit: "))
        if acc in accounts:
            accounts[acc] += amt
            print("Deposited to the account")
        else:
            print("Account not found.")
    elif ch == 2:
        acc = input("enter the acc number: ")
        amt = int(input("Enter the amount to withdraw: "))
        if acc in accounts:
            if accounts[acc] >= amt:
                accounts[acc] -= amt
                print("Withdrawn from the account")
            else:
                print("Insufficient balance")
        else:
            print("Account not found.")
    elif ch == 3:
        acc_from = input("Enter the account number to transfer from: ")
        acc_to = input("Enter the account number to transfer to: ")
        amt = int(input("Enter the amount to transfer: "))
        if acc_from in accounts and acc_to in accounts:
            if accounts[acc_from] >= amt:
                accounts[acc_from] -= amt
                accounts[acc_to] += amt
                print("Transfer successful.")
            else:
                print("Insufficient balance for transfer.")
        else:
            print("One or both account numbers not found.")
    elif ch == 4:
        acc = input("enter the acc number: ")
        if acc in accounts:
            print(f"Balance for account {acc}: {accounts[acc]}")
        else:
            print("Account not found.")
    elif ch == 5:
        print("Logging out...")
        break
    else:
        print("Invalid choice, please try again.")
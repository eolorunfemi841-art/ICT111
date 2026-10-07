accounts = {
    "0971111111": {"password": "1234", "balance": 1000},
    "0972222222": {"password": "abcd", "balance": 500},}
transactions = []

print("-- Welcome to Airtel Mobile Money --")

#MAIN MENU
while True:
    print("")
    print("1. Log in") 
    print("2. Create account")
    print("3. Exit")
    choice = input("Choose between 1-3: ")

    #  LOG IN 
    if choice == "1":
        phone = input("Enter your phone number: ")
        password = input("Enter your password: ") 

       
        if phone in accounts and accounts[phone]["password"] == password:
            print("=============== Welcome " + phone + " ===============")

            # USER MENU 
            while True:
                print("")
                print("1. View balance")
                print("2. Send money to another number")
                print("3. Deposit money")
                print("4. View transaction history")
                print("5. Reverse last transaction")
                print("6. Change password")
                print("7. Log out")
                option = input("Select an option from 1 to 7: ")

                #  1. VIEW BALANCE
                if option == "1":
                    print("Your balance is: K" + str(accounts[phone]["balance"]))

                # 2. SEND MONEY 
                elif option == "2":
                    receiver = input("Enter the number you want to send to: ")

                    if receiver not in accounts:
                        print("That number is not registered.")
                    elif receiver == phone:
                        print("You cannot send money to yourself.")
                    else:
                        amountText = input("Enter the amount you wish to send: K")

                        # isdigit() is True only if the text is whole numbers (no letters)
                        if not amountText.isdigit():
                            print("Please enter numbers only.")
                        else:
                            amount = int(amountText)

                            if amount == 0:
                                print("The amount must be more than 0.")
                            elif amount > accounts[phone]["balance"]:
                                print("You don't have enough money.")
                            else:
                                # Take money from sender, give it to receiver
                                accounts[phone]["balance"] = accounts[phone]["balance"]  #the sender's balance is updated by subtracting the amount sent
                                accounts[receiver]["balance"] = accounts[receiver]["balance"] #the receiver's balance is updated by adding the amount sent
                                # Save the transaction
                                transactions.append({ "id": len(transactions) + 1,"type": "send","sender": phone,"receiver": receiver, "amount": amount,"reversed": False})
                                print("===========================")
                                print("Transaction was successful")
                                print("===========================")

                # 3. DEPOSIT MONEY
                elif option == "3":
                    amountText = input("Enter the amount you wish to deposit: K")

                    if not amountText.isdigit():
                        print("Please enter numbers only.")
                    else:
                        amount = int(amountText)

                        if amount == 0:
                            print("The amount must be more than 0.")
                        else:
                            accounts[phone]["balance"] = accounts[phone]["balance"] + amount 
                            transactions.append({"id": len(transactions) + 1,"type": "deposit","sender": "CASH","receiver": phone,"amount": amount,"reversed": False})
                            print("===========================")
                            print("Deposit was approved")
                            print("New balance: K" + str(accounts[phone]["balance"]))
                            print("===========================")

                # 4. VIEW TRANSACTION HISTORY
                elif option == "4":
                    print("---- Transaction history for " + phone + " ----")
                    found = False

                    for t in transactions:
                        # Only show transactions this user was part of
                        if t["sender"] == phone or t["receiver"] == phone:
                            found = True

                            if t["type"] == "deposit":
                                text = "#" + str(t["id"]) + " Deposited K" + str(t["amount"])
                            elif t["sender"] == phone:
                                text = "#" + str(t["id"]) + " Sent K" + str(t["amount"]) + " to " + t["receiver"]
                            else:
                                text = "#" + str(t["id"]) + " Received K" + str(t["amount"]) + " from " + t["sender"]

                            if t["reversed"]:
                                text = text + "  [REVERSED]"
                            print(text)

                    if found == False:
                        print("You have no transactions yet.")

                # 5. REVERSE LAST TRANSACTION 
                elif option == "5":
                    # Find the LATEST money this user sent that is not reversed yet.
                    last = None
                    for t in transactions:
                        if t["type"] == "send" and t["sender"] == phone and t["reversed"] == False:
                            last = t

                    if last == None:
                        print("You have no transaction to reverse.")
                    else:
                        print("Last transaction: K" + str(last["amount"]) + " sent to " + last["receiver"])

                        # The receiver must still have the money
                        if accounts[last["receiver"]]["balance"] < last["amount"]:
                            print("Cannot reverse: the receiver no longer has enough money.")
                        else:
                            confirm = input("Reverse this transaction? (yes/no): ")

                            if confirm.lower() == "yes":
                                accounts[last["receiver"]]["balance"] = accounts[last["receiver"]]["balance"] - last["amount"]
                                accounts[phone]["balance"] = accounts[phone]["balance"] + last["amount"]
                                last["reversed"] = True
                                print("Transaction reversed. Your money is back.")
                            else:
                                print("Reversal cancelled.")

                #  6. CHANGE PASSWORD
                elif option == "6":
                    oldPassword = input("Enter your current password: ")

                    if oldPassword != accounts[phone]["password"]:
                        print("Wrong password.")
                    else:
                        newPassword = input("Enter a new password: ")

                        if newPassword == oldPassword:
                            print("The new password is the same as the old one :)")
                        else:
                            again = input("Enter the new password again: ")

                            if newPassword != again:
                                print("The passwords do not match.")
                            else:
                                accounts[phone]["password"] = newPassword
                                print("===========================")
                                print("Password has been changed")
                                print("===========================")

                # 7. LOG OUT 
                elif option == "7":
                    print("You have been logged out.")
                    break   # leaves the user menu and goes back to the main menu

                else:
                    print("Invalid option, try again.")

        else:
            print("Incorrect phone number or password.")

    # CREATE ACCOUNT 
    elif choice == "2":
        newPhone = input("Enter a new phone number (10 digits): ")

        if not newPhone.isdigit() or len(newPhone) != 10:
            print("Invalid number. Use exactly 10 digits.")
        elif newPhone in accounts:
            print("That number is already registered.")
        else:
            newPassword = input("Create a password: ")

            if newPassword == "":
                print("Password cannot be empty.")
            else:
                # New accounts start with K0
                accounts[newPhone] = {"password": newPassword, "balance": 0}
                print("Account created! You can now log in.")

    #  EXIT 
    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice, try again.")
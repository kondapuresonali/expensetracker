expensesList = []  # list of expenses in the form of dictionaries
print("welcome to expenses tacker: kharcha kam kiya karo")

while True:

    print("\n=====MENU=====")
    print("\n1. Add Expense")
    print("\n2. View all Expenses")
    print("\n3. View total Expenses")
    print("\n4. Exit")

    choice = int(input("\nplease enter your choice: "))

    # ADD EXPENSES
    if (choice == 1):
        date = input("enter the date of expense : ")
        category = input("enter the type of expenses? (food,makeup.stationary,education,travel)")
        description = input("detail of the expenses ")
        amount = float(input("enter the amount : "))

        expense = {
            "date": date,
            "category": category,
            "description": description,
            "amount": amount
        }

        expensesList.append(expense)
        print("\n DONE. expense is added successfully")

    # 2 view all expenses
    elif choice == 2:
        if (len(expensesList) == 0):
            print("no expenses added. go for shopping. ")
        else:
            print("===== this is all expenses i made")
            count = 1
            for eachexpense in expensesList:
                print(
                    f"expense number {count}->  "
                    f"{eachexpense['date']},"
                    f"{eachexpense['category']},"
                    f"{eachexpense['description']},"
                    f"{eachexpense['amount']}"
                )
                count = count + 1

    # 3 view total spending
    elif choice == 3:
        total = 0
        for eachexpense in expensesList:
            total = total + eachexpense["amount"]
        print("\n TOTAL expense = ", total)

    # 4 exit
    elif (choice == 4):
        print("thanku for using aur system")
        break

    else:
        print("INVALID.TRY AGAIN")

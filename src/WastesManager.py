import  src.Tools as tools
import  src.DataManager as dm

def add_wastes_menu() -> None:
    name: str = ''
    money_sum: float | str = 0.0
    date: str = ''
    while True:
        print("Adding a new expense...   Input '-1' to exit.\nInput expense's name")
        name = input("User input: ")

        if name == '-1':
            print('\n\n\n')
            return

        if name.find('\n') != -1 or name.find('~') != -1:
            print("Input need to be without 'enter' keyword or symbol '~'.")
        else:
            print('\n\n\n')
            break

    while True:
        print("Adding a new expense...   Input '-1' to exit.\nInput expense's cost")
        money_sum_raw: str = input("User input: ")

        if money_sum_raw == '-1':
            print('\n\n\n')
            return

        money_sum = tools.make_numeric(money_sum_raw)

        # make_numeric returns -1.0 on failure
        if money_sum == -1.0:
            print("Input need to be numeric.")
        else:
            print('\n\n\n')
            break

    while True:
        print("Adding a new expense...   Input '-1' to exit.\nInput expense's date")
        date = input()

        if date == '-1':
            print('\n\n\n')
            return

        if date.find('\n') != -1 or date.find('~') != -1:
            print("Input need to be without 'enter' keyword or symbol '~'.")
        else:
            print('\n\n\n')
            break

    money_sum = str(money_sum)
    if dm.edit_expenses((name, money_sum, date)) == -1:
        print('Problems with saving Expenses file...\nReturing to expenses menu.\n')
    else:
        print('\n\n\nNew expense added!\n')

    input("Enter to continue ")
    print("\n\n\n")

def show_wastes(is_from_rm_menu: bool = False, exp_cnt: int = 0) -> None:
    wastes = dm.load_wastes()
    total: float = 0.0
    expense_cnt: int = 0

    if wastes is None:
        if not is_from_rm_menu:
            print('File not found\n')
    else:
        print(f'Your Wastes and Total:\n{"№".ljust(7)}  {"Name:".ljust(30)}  {"Cost:".ljust(20)}  {"Date:".ljust(1)}')
        for waste in wastes:
            expense = waste.split('~')

            if len(expense) != 3:
                continue

            expense_cnt += 1
            name, money_sum, date = expense
            total += tools.make_numeric(money_sum.strip())
            print(f"#{expense_cnt:<6}  {name.ljust(30)}  {(str(tools.make_numeric(money_sum)) + " BYN").ljust(20)}  {date.rstrip('\n').ljust(1)}")

        print(f'In Total: {total:>10} BYN\n')

    if not is_from_rm_menu:
        answer = input("Enter to continue ")
        print("\n\n\n")
        return

    while True:
        print('Enter id of expense to remove or input "exit" to return to menu: ')
        answer = input('User answer: ')

        if answer == 'exit':
            print('\n\n\n')
            return

        answer = tools.check_answer_valid(answer)

        print('\n\n\n')
        if answer == -1 or answer > exp_cnt or answer < 1:
            print("You need to enter a valid id.")
            continue
    
        for i in range(1, exp_cnt + 1):
            if answer == i:
                if dm.remove_expense(answer) == -1:
                    print("File problems...\n")
                else:
                    print("Expense removed.\n")

                input("Enter to continue ")
                print('\n\n\n')
                return

def show_remove_expense_menu() -> None:
    expenses = dm.load_wastes()

    if expenses is None:
        print('There is no expenses to delete.\n\n')
        input("Enter to continue ")
        return

    exp_cnt = 0

    for expense in expenses:
        info = expense.split('~')
        if len(info) == 3:
            exp_cnt += 1

    if exp_cnt == 0:
        print('There is no expenses to delete.\n\n')
        input("Enter to continue ")
        return

    show_wastes(True, exp_cnt)

def show_wastes_menu() -> None:
    while True:
        print("Wastes Menu\nChoose an option:\n1) Check wastes\n2) Add wastes\n3) Remove expense\n4) Return to main menu")

        choice: int = tools.check_answer_valid(input("User input: "))

        if choice == 1:
            print('\n\n\n')
            show_wastes()
        elif choice == 2:
            print('\n\n\n')
            add_wastes_menu()
        elif choice == 3:
            print('\n\n\n')
            show_remove_expense_menu()
        elif choice == 4:
            print('\n\n\n')
            return
        else:
            print("You have to enter a valid option\n\n\n")

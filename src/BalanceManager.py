import src.DataManager as dm
import src.Tools as tools

def edit_balance_menu(balance: list[float], curr_id: int) -> None:
    while True:
        user_answer = input("Input new amount or exit with 'exit': ")

        if user_answer == 'exit':
            if dm.edit_balance_data(balance) == -1:
                print("\n\n\nProblems with saving balance...\n")

                input("Enter to continue ")
                print("\n\n\n")
            return

        try:
            money_amount = float(user_answer)
        except ValueError:
            print("Please enter a numeric value.\n")
        else:
            balance[curr_id] = money_amount
            if dm.edit_balance_data(balance) == -1:
                print("\n\n\nProblems with saving balance...\n")

        input("Enter to continue ")
        print("\n\n\n")

        return

def show_edit_balance_menu() -> None:
    user_answer: int = 0
    money_amount: float = 0.0

    balance = dm.load_balance_data()
    if balance is None:
        balance = [0.0, 0.0, 0.0]

    while True:
        print("Choose balance currency to edit:")
        print("1) Belarusian\n2) Dollar USA\n3) Rusian\n4) Exit")

        raw: str = input("User input: ")
        user_answer = tools.check_answer_valid(raw)

        if user_answer == 1:
            print('\n\n\n')
            print(f"Belarusian: {balance[0]:.2f}")
            edit_balance_menu(balance, 0)
            print('\n\n\n')
            show_balance(True)
        elif user_answer == 2:
            print('\n\n\n')
            print(f"Dollar USA: {balance[1]:.2f}")
            edit_balance_menu(balance, 1)
            print('\n\n\n')
            show_balance(True)
        elif user_answer == 3:
            print('\n\n\n')
            print(f"Rusian: {balance[2]:.2f}")
            edit_balance_menu(balance, 2)
            print('\n\n\n')
            show_balance(True)
        elif user_answer == 4:
            print('\n\n\n')
            return
        else:
            print("You have to enter a valid option.")

def show_balance(exec_from_edit: bool = False) -> None:
    balance = dm.load_balance_data()
    if balance is None:
        print("File with balance has been corrupted:\nNot found, or too many field for currencies\n")
    else:
        if exec_from_edit:
            print("Your new balance:")
        else:
            print("Your balance:")

        print(f"{'Belarusian:'.ljust(13)} {balance[0]:.2f}")
        print(f"{'Dollar USA:'.ljust(13)} {balance[1]:.2f}")
        print(f"{'Rusian:'.ljust(13)} {balance[2]:.2f}\n")

    answer = input("Enter to continue ")
    print("\n\n\n")

def show_balance_menu() -> None:
    user_answer: int = 0

    while True:
        print("Balance Manager\nChoose an option:")
        print("1) Check balance\n2) Edit balance\n3) Return to main menu")

        raw: str = input("User input: ")
        user_answer = tools.check_answer_valid(raw)

        if user_answer == 1:
            print('\n\n\n')
            show_balance()
        elif user_answer == 2:
            print('\n\n\n')
            show_edit_balance_menu()
        elif user_answer == 3:
            print('\n\n\n')
            return
        else:
            print("\n\n\nYou have to enter a valid option.")

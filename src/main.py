import sys
import src.BalanceManager as bm
import src.Tools as tools
import src.WastesManager as wm

first_vis: bool = False

def show_menu() -> None:
    user_answer: int = 0
    global first_vis

    if not first_vis:
        print("Hello! You are in Finances Manager\nYou can track your balance and wastes here.")
    first_vis = True

    while True:
        print("Main Menu\nChoose an option:\n1) View balance\n2) View wastes\n3) Exit")

        raw: str = input("User input: ")
        user_answer = tools.check_answer_valid(raw)

        if user_answer == 1:
            print("\n\n\n")
            bm.show_balance_menu()
        elif user_answer == 2:
            print("\n\n\n")
            wm.show_wastes_menu()
        elif user_answer == 3:
            print("\n\n\n")
            print("Exiting...")
            sys.exit()
        else:
            print("\n\n\nYou have to enter a valid option.")



show_menu()

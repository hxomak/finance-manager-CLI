from src.Tools import balance_file_path
from src.Tools import expenses_file_path

def edit_balance_data(curr_list: list[float]) -> int:
    try:
        with open(balance_file_path, "w") as f:
            for curr in curr_list:
                f.write(str(curr) + '\n')
    except FileNotFoundError:
        return -1
    return 0

def load_balance_data() -> list[float] | None:
    curr_cnt: int = 0
    curr_list: list[float] = []

    try:
        with open(balance_file_path, "r") as f:
            for curr in f:
                curr_cnt += 1
                try:
                    curr_list.append(float(curr.strip()))
                except ValueError:
                    curr_list.append(0.0)
                except BaseException:
                    curr_list.append(0.0)

        if curr_cnt > 3:
            return None
        if curr_cnt < 3:
            for i in range(curr_cnt + 1, 4):
                curr_list.append(0.0)
    except FileNotFoundError:
        return None

    return curr_list

def load_wastes() -> list[str] | None:
    try:
        with open(expenses_file_path, "r") as f:
            return f.readlines()
    except FileNotFoundError:
        return None

def edit_expenses(data: tuple[str, str, str]) -> int:
    try:
        with open(expenses_file_path, "a") as f:
            new_expense = '~'.join(data)
            f.seek(0, 1)
            f.write('\n' + new_expense)

            return 0

    except FileNotFoundError:
        return -1

def export_edited_expenses(expenses: list[str]) -> int:
    try:
        with open(expenses_file_path, "w") as f:
            f.writelines(expenses)
            return 0
    except FileNotFoundError:
        return -1

def remove_expense(exp_id: int) -> int:
    # Remove expense by 1-based index among valid expense lines (lines with 3 '~'-separated parts).
    try:
        with open(expenses_file_path, "r") as f:
            expenses = f.readlines()
    except FileNotFoundError:
        return -1

    kept_lines: list[str] = []
    current_idx = 0
    removed = False

    for line in expenses:
        parts = line.rstrip('\n').split('~')
        # If the line does not represent a valid expense, keep it as-is and do not count it
        if len(parts) != 3:
            kept_lines.append(line)
            continue

        current_idx += 1
        if current_idx == exp_id:
            # skip this line -> effectively delete
            removed = True
            continue

        # normalize line to ensure single terminating newline
        kept_lines.append('~'.join(parts) + '\n')

    if not removed:
        # requested id not found
        return -1

    return export_edited_expenses(kept_lines)


balance_file_path: str = '../data/Balance.txt'
expenses_file_path: str = '../data/Expenses.txt'

def check_answer_valid(answer: str) -> int:
    try:
        answer = int(answer)
    except (ValueError, BaseException):
        return -1
    else:
        return answer

def make_numeric(num: str) -> float:
    """Parse a string to float. Returns -1.0 on failure."""
    try:
        return float(num)
    except ValueError:
        return -1.0

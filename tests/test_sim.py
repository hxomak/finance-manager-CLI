# simulate remove_expense logic locally
lines = open('../data/Expenses.txt', 'r', encoding='utf-8').readlines()
exp_id = 2
kept_lines = []
current_idx = 0
removed = False
for line in lines:
    parts = line.rstrip('\n').split('~')
    print('line repr:', repr(line), 'parts:', parts)
    if len(parts) != 3:
        kept_lines.append(line)
        continue
    current_idx += 1
    print('current_idx now', current_idx)
    if current_idx == exp_id:
        removed = True
        print('will remove this line')
        continue
    kept_lines.append('~'.join(parts) + '\n')

print('removed=', removed)
print('kept_lines:', kept_lines)


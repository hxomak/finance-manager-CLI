lines = open('../data/Expenses.txt', 'r', encoding='utf-8').readlines()
print('lines repr:', [repr(l) for l in lines])
for i, line in enumerate(lines, 1):
    parts = line.rstrip('\n').split('~')
    print(i, 'parts:', parts, 'len:', len(parts))


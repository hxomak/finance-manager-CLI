import importlib.util
import sys
from pathlib import Path

# load DataManager module by path
spec = importlib.util.spec_from_file_location('dm', '../src/DataManager.py')
dm = importlib.util.module_from_spec(spec)
spec.loader.exec_module(dm)

# prepare test data
p = Path('../data')
p.mkdir(exist_ok=True)
with open(p / 'Expenses.txt', 'w', encoding='utf-8') as f:
    f.write('coffee~2.5~2026-06-01\n')
    f.write('lunch~10.0~2026-06-02\n')
    f.write('snacks~1.5~2026-06-03\n')

print('Before:')
print(open(p / 'Expenses.txt', encoding='utf-8').read())

res = dm.remove_expense(2)
print('remove_expense returned', res)

print('After:')
print(open(p / 'Expenses.txt', encoding='utf-8').read())


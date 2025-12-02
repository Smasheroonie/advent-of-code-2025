input = open("input.txt").read().strip().split(',')

pairs = []
even_len = []
total = 0

for i in input:
    pairs.append(i.split('-'))

for i in pairs:
    for j in range(int(i[0]), int(i[1])):
        if len(str(j)) % 2 == 0:
            even_len.append(j)

for i in even_len:
    s_i = str(i)
    q, r = divmod(len(s_i), 2)
    first, second = s_i[:q + r], s_i[q + r:]
    if first == second:
        pattern = ''.join((first, second))
        total += int(pattern)

print(total)

'''
Simplified:

total = 0
for pair in open("input.txt").read().strip().split(','):
    start, end = map(int, pair.split('-'))
    for num in range(start, end):
        s_num = str(num)
        if len(s_num) % 2 == 0 and s_num[:len(s_num)//2] == s_num[len(s_num)//2:]:
            total += num
print(total)

---

Using regex:

import re

total = 0
pattern = re.compile(r'^(\d+)\1$')

for pair in open("input.txt").read().strip().split(','):
    start, end = map(int, pair.split('-'))

    for num in range(start, end):
        s_num = str(num)
        if pattern.fullmatch(s_num):
            total += num
print(total)

'''
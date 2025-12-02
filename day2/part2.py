input = open("input.txt").read().strip().split(',')

pairs = []
even_len = []
odd_len = []
total = 0

for i in input:
    pairs.append(i.split('-'))

for i in pairs:
    for j in range(int(i[0]), int(i[1]) + 1):
        if len(str(j)) % 2 == 0:
            even_len.append(j)
        elif len(str(j)) % 2 != 0 and len(str(j)) > 1:
            odd_len.append(j)
        
for i in even_len:
    s_i = str(i)
    if len(s_i) == 6 and ''.join((s_i[0], s_i[1])) == ''.join((s_i[2], s_i[3])) == ''.join((s_i[4], s_i[5])):
        total += int(s_i)
    elif len(s_i) == 10 and ''.join((s_i[0], s_i[1])) == ''.join((s_i[2], s_i[3])) == ''.join((s_i[4], s_i[5])) == ''.join((s_i[6], s_i[7])) == ''.join((s_i[8], s_i[9])):
        total += int(s_i)
    else:
        q, r = divmod(len(s_i), 2)
        first, second = s_i[:q + r], s_i[q + r:]
        if first == second:
            pattern = ''.join((first, second))
            total += int(pattern)

for i in odd_len:
    s_i = str(i)
    if len(s_i) == 9:
        if ''.join((s_i[0], s_i[1], s_i[2])) == ''.join((s_i[3], s_i[4], s_i[5])) == ''.join((s_i[6], s_i[7], s_i[8])):
            total += int(s_i)
    num = ''
    j = 0
    while j < len(s_i) - 1:
        if s_i[j] == s_i[j+1]:
            num = num + s_i[j]
        j += 1
    if len(num) == len(s_i) - 1 and s_i[j] == s_i[j-1]:
        num = num + s_i[j]
        total += int(num) 

print(total)

'''
Simplified:

total = 0
for pair in open("input.txt").read().strip().split(','):
    start, end = map(int, pair.split('-'))
    
    for num in range(start, end + 1):
        s_num = str(num)
        length = len(s_num)
        
        # Handle even-length numbers
        if length % 2 == 0:
            if length == 6:
                if s_num[:2] == s_num[2:4] == s_num[4:6]:
                    total += num
            elif length == 10:
                if s_num[:2] == s_num[2:4] == s_num[4:6] == s_num[6:8] == s_num[8:10]:
                    total += num
            else:
                half = length // 2
                if s_num[:half] == s_num[half:]:
                    total += num
        
        # Handle odd-length numbers > 1
        elif length > 1 and length % 2 != 0:
            if length == 9:
                if s_num[:3] == s_num[3:6] == s_num[6:9]:
                    total += num
            else:
                # Check for consecutive duplicates
                has_consecutive = any(s_num[i] == s_num[i+1] for i in range(len(s_num)-1))
                if has_consecutive:
                    total += num

print(total)

---

using regex:

import re

total = 0
pattern = re.compile(r'^(\d+)\1+$')

for pair in open("input.txt").read().strip().split(','):
    start, end = map(int, pair.split('-'))
    
    for num in range(start, end + 1):
        s_num = str(num)
        # Check if the entire number consists of a repeating pattern
        if pattern.fullmatch(s_num):
            total += num

print(total)

'''
input = open("input.txt").read().split()

# joltage = 0
# loop = 0

# for bank in input:

#     loop +=1
#     print(f'Loop: {loop}')


#     def jolt_sort(sequence = list(bank[88:]), largest = str(max(bank[:89])), position = 0):

#         joltage = 0

#         if position == 12:
#             joltage += int(''.join(sequence))
#             return joltage
#         else:
#             start = bank.index(largest) # index of first instance of the highest number in the range of positions 0 to 87 (first 88)
#             sequence[position] = bank[start] # first entry in the sequence changes to the max 
#             position += 1
#             if start < 99:
#                 largest = str(max(bank[start+1:89+position])) # largest assigned to highest number in the bank in a range from the next index after the largest number 
#             else:
#                 largest = str(max(bank[99:]))
#             jolt_sort(sequence, largest, position)

#     jolt_sort()

def chk(ss,k):
    if k==0:return ''
    mx=max(ss[:len(ss)-k+1])
    pm=ss.index(mx)
    return mx+chk(ss[pm+1:],k-1)
ans=sum(int(chk(s,12)) for s in input)
print('part2',ans)
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

def battery_sort(bank, num_of_batteries):

    if num_of_batteries == 0:
        return '' # if we get to the end of the battery bank, end the recursive loop
    
    max_range = len(bank) - num_of_batteries + 1 # the index to be the end of the range. 1st loop: range = 100 - 13 = 87, 2nd loop: remaining bank - 12, etc.
    max_value = max(bank[:max_range]) # find the largest number (highest joltage) in the range
    position = bank.index(max_value) # the position of the largest number
    remaining_bank = bank[position + 1:] # the rest of the bank from the position of the number after largest number

    highest_total_joltage = max_value + battery_sort(remaining_bank, num_of_batteries - 1) # recursive call, return max value + the max value from the next loop, until end of sequence (bank)
    if len(highest_total_joltage) == 12: print(highest_total_joltage)
    return highest_total_joltage

joltage = sum(int(battery_sort(bank, 12)) for bank in input) # add up all the highest joltages for the answer
print('Joltage:', joltage)

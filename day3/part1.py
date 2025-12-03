input = open("input.txt").read().split()

joltage = 0

for bank in input:

    largest = str(max(bank))
    
    index_of_largest = bank.index(largest)

    if index_of_largest == 99:
        max_l = str(max(bank[:99]))
        joltage += int(max_l + largest)
    elif index_of_largest == 0:
        max_r = str(max(bank[0:]))
        joltage += int(largest + max_r)
    else:
        max_l = str(max(bank[:index_of_largest]))
        max_r = str(max(bank[index_of_largest+1:]))
        if int(max_l + largest) > int(largest + max_r):
           joltage += int(max_l + largest)
            
        else:
           joltage += int(largest + max_r)

print(joltage)
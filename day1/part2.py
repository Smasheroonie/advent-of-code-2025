input = open("input.txt").read().split()

zero_counter = 0
position = 50

for instruction in input:

    rotation = int(instruction[1:])

    if rotation > 99:
        zero_counter += int(str(rotation)[:1])
        rotation = int(str(rotation)[1:])

    if instruction.startswith("R"):
        position += rotation
    elif instruction.startswith("L"):
        position -= rotation
    
    if position > 99:
        position = position - 100
        zero_counter += 1
    elif position < 0:
        position = position + 100
        zero_counter += 1

    print(zero_counter)
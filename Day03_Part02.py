# !/usr/bin/python3
# AdventOfCode2022 - Day03 Part02


f = open("Day03-input.txt")
data = f.read().split("\n")
f.close()
data = list(filter(None, data))  # to filter out blanks

priority = 0
for i in range(0, len(data), 3):
    Elf1 = data[i]
    Elf2 = data[i+1]
    Elf3 = data[i+2]
    common_characters = "".join(set(Elf1).intersection(Elf2).intersection(Elf3))

    for j in common_characters:
        if ord(j) > 90:  # small character
            priority += ord(j) - 96
        else:
            priority += ord(j) - 38

print(priority)


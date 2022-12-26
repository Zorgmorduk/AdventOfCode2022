# !/usr/bin/python3
# AdventOfCode2022 - Day03 Part01


f = open("Day03-input.txt")
data = f.read().split("\n")
f.close()
data = list(filter(None, data))  # to filter out blanks

priority = 0
for i in data:
    compartment1 = i[0:len(i)//2]
    compartment2 = i[len(i)//2:]
    common_characters = "".join(set(compartment1).intersection(compartment2))

    for j in common_characters:
        if ord(j) > 90:  # small character
            priority += ord(j) - 96
        else:
            priority += ord(j) - 38

print(priority)


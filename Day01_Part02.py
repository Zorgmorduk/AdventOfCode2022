# !/usr/bin/python3
# AdventOfCode2022 - Day01 Part02


f = open("input.txt")
data = f.read().split("\n")
f.close()

calories_per_elf = []
calorie_counter = 0
for value in data:
    if value == "":
        calories_per_elf.append(calorie_counter)
        calorie_counter = 0
    else:
        calorie_counter += int(value)


calories_per_elf.sort(reverse=True)
print(sum(calories_per_elf[:3]))

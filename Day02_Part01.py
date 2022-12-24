# !/usr/bin/python3
# AdventOfCode2022 - Day02 Part01


f = open("Day02-input.txt")
data = f.read().split("\n")
f.close()
data = list(filter(None, data))  # to filter out blanks
opponent, response = [], []
score = 0
for i in data:
    opponent.append(i[0:1])
    response.append(i[2:3])
    if response[-1] == "X":
        score += 1
    elif response[-1] == "Y":
        score += 2
    else:
        score += 3

    if opponent[-1] == "A" and response[-1] == "X":
        score += 3  # draw
    elif opponent[-1] == "B" and response[-1] == "Y":
        score += 3  # draw
    elif opponent[-1] == "C" and response[-1] == "Z":
        score += 3  # draw
    elif opponent[-1] == "A" and response[-1] == "Y":
        score += 6  # win
    elif opponent[-1] == "B" and response[-1] == "Z":
        score += 6  # win
    elif opponent[-1] == "C" and response[-1] == "X":
        score += 6  # win
    else:
        score += 0  # loss


print(score)

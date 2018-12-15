#!/usr/bin/env python3

# collections -> Counter.... could be used to easily improve this... oh well.

from collections import defaultdict

with open("day2_input") as data:
    data = data.read().split()

letter_count = {}
contenders = {2:0, 3:0}

# Get letter counts of each line.
for index, line in enumerate(data):
    letter_count[index]= defaultdict(int)

    for char in line:
        letter_count[index][char] += 1

# Get counts that have one with 2 chars and/or 3 chars
for index, line in enumerate(letter_count):
    counts = str(letter_count[index].values())
    instances_of_2 = counts.count("2")
    instances_of_3 = counts.count("3")

    if instances_of_2 >= 1:
        contenders[2] += 1
    if instances_of_3 >= 1:
        contenders[3] += 1

print(contenders[2] * contenders[3])

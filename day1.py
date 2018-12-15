#! /usr/bin/env python3
with open("day1_input") as data:
    lines = data.read().split()

print(sum([int(line) for line in lines]))

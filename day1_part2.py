#! /usr/bin/env python3
# with open("day1_input") as data:
with open("day1_input") as data:
    lines = data.read().split()

lines = [int(line) for line in lines]

# initialize tracking of values.
frequency = 0
index = 0
end = len(lines)
tracker = {0:1}

# loop through list until a freq of two happens.
while True:
    frequency += lines[index]
    
    try:  # Should be second time seeing frequency
        tracker[frequency] += 1
        print(frequency)
        break
    except KeyError:  # should be first time seeing frequency
        tracker[frequency] = 1
    
    index += 1
    
    if index == end:
        index = 0

#!/usr/bin/env python3

from collections import defaultdict

def main():
    """
    Line Example From Data
    #632 @ 143,278: 22x17
    1. Claim ID
    2. 143, 278 -> 143 from left edge, 278 from top. (from top left to bottom right)
    3. 22 units WIDE, 17 units HIGH

    The whole 'cloth' is _at least_ 1000x1000 -- Let's go for 1.1k square to play it safe, eh?
    """
    with open("day3_input") as data:    
        data = data.read().split("\n")

    overlaps = 0
    occupied_coords = defaultdict(int)  #  0 is unoccupied. if it is 2 or greater that's the number of overlaps, eh? defaultdict starts with 0 for int
    
    # Go through the cords. Add 1 to the value.
    # Need a for for all the lines and then another for to get the patch that's declared.
    for coord in data:
        patch = tuple(coord.split()[3].split("x"))  # Getting a tuple of the patch's size
        spot = tuple(coord.split()[2].replace(":","").split(","))
        
        for x_index, x in enumerate(range(int(patch[0]))):
            for y_index, y in enumerate(range(int(patch[1]))):
                # Have the columns here. Fill in the occupied_coords here.
                current_spot = tuple([int(spot[0]) + x_index, int(spot[1]) + y_index])

                occupied_coords[current_spot] += 1
                # print("\tAdded 1 to coords. Current value of {} is {}".format(current_spot, occupied_coords[current_spot]))

                # if occupied_coords[current_spot] > 1:
                if occupied_coords[current_spot] == 2:  # 
                    # print("Overlapped spot!", current_spot)
                    overlaps += 1

    return occupied_coords, overlaps, data


def solid_section(occupied_coords, data):
    """
    Go through the data again. Find a section where the occupied_data for square inch is == 1.
    data -> instructions
    occupied_coords -> spots that are in use -> where the value of the key is number of times the spot is overlapped.

    This part is gross.
    """
    # Go through the cords. change toggle variable when a section is alone
    # Need a for for all the lines and then another for to get the patch that's declared.
    for coord in data:
        patch = tuple(coord.split()[3].split("x"))  # Getting a tuple of the patch's size
        spot = tuple(coord.split()[2].replace(":","").split(","))
        plot_ID = coord.split()[0]

        alone = True  # Not overlapped toggle
        length = int(patch[0]) - 1

        for x_index, x in enumerate(range(int(patch[0]))):
            for y_index, y in enumerate(range(int(patch[1]))):
                # Have the columns here. Fill in the occupied_coords here.
                current_spot = tuple([int(spot[0]) + x_index, int(spot[1]) + y_index])
                if occupied_coords[current_spot] != 1:
                    # Here's liekly an overlap here. Move on to the next patch...
                    # Would need another variable to manage skipping the rest. Eh...
                    alone = False

        if x_index == length:
            # hit the end of the patch. Was thewre no overlaps?
            if alone is True:
                print(plot_ID)
                alone = True
            
            # input()


# def visualizer(occupied_coords):
#     coords = [(x, y) for x in range(1100) for y in range(1100)]


occupied_coords, overlaps, data = main()
# print("Overlaps:", overlaps)
# visualizer(occupied_coords)
solid_section(occupied_coords, data)

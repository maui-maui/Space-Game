"""
Tools for Generating Sectors and Quadrants

Contains:
    generate_sector - Generates an Sector
    generate_quadrant - Generates an Quadrant
"""

import random

# TODO: Add Error Catching when no @ got Generated
def generate_sector(size: int) -> list:
    """
    Generates an Sector Map File

    generate_sector(9) would generate an 9x9 Map

    Parameters
    ----------
    size: Int Representing the Size of the Generated Map

    Returns
    -------
    An Nested Array with the Map Data
    """
    output = []
    map_objects = ["*", "P", "C", "!", "^", "B", "@", "#"]
    placed_player = False

    for x in range(size):
        row = []
        for y in range(size):
            choice = random.choice(map_objects)
            if choice is "@" and placed_player is False:
                row.append(choice)
                placed_player = True
                continue
            elif choice is "@" and placed_player is True:
                row.append("*")
                continue
            else:
                row.append(choice)
        output.append(row)
    return output


def generate_quadrant(size: int) -> list:
    pass
print(mapgen())
"""
An Util which has Utilitys to generate an Text Based Map

Contains:
    Generate Sector: An Map Generator which Generates an Weighted Map Grid
    Visualise Sector: Takes an Map Grid and Prints it out in an Human Readable form
    Generate Quadrant: An Map Generator which generates basicly an "Galaxy" where Sectors are in
"""

import bisect
import random

import colorama
from colorama import Fore

colorama.init()


def generate_sector(size: int, object_weight: list) -> dict:
    """
    Generates an Sector with Weighted Spawns

    Args:
        size: Int Representing the Size of the Sector (Size X Size)
        object_weight: An Nested List with Object / Value Types

    Examples:
        generate_sector(6, [["*", 50], ["#", 10]]) would output an Map File where * is far more Common than #

    Returns:
        An Dict with Lists inside which Represent the Map Data per Row
    """

    if size is 0:
        raise ValueError("The Sector Size cant be 0")

    size += 1

    output = {}
    placed_player = False
    totals = []
    running_total = 0

    for w in object_weight:
        running_total += w[1]
        totals.append(running_total)

    def next():
        """
        Gets an Random Object from the Object - Weight List
        """
        ran = random.random() * totals[-1]
        i = bisect.bisect_right(totals, ran)
        return object_weight[i][0]

    for x in range(1, size):
        row = []
        for y in range(1, size):
            object = next()
            if placed_player is False and object is "@":
                row.append(object)
                placed_player = True
                continue
            elif placed_player is True and object is "@":
                while object is "@":
                    object = next()
            row.append(object)
        output[x] = row
    return output


def generate_quadrant(sector_size: int, quadrant_size: int, object_weight: list) -> dict:
    """
    Generates an Quadrant based upon Generate Sector
    Args:
        sector_size: Int Representing the Size of the Sector (Size X Size)
        quadrant_size: Int Representing the Amount of Quadrants, Has to be Divisable by 2
        object_weight: An Nested List with Object / Value Types

    Examples:
        generate_quadrant(6, 2, [["*", 50], ["#", 10]]) would generate an Dict with 2 Quadrants who each have 1 Sector
        (Look into generate_sector for more Information on how Sectors are Used)

    Returns:
        An Dict with Keys based Upon Quadrant Number (NOT Zero Indexed) which Contain an Sector Dict (See
        generate_sector for more info)
    """
    if quadrant_size is 0:
        raise ValueError("The Quadrant Size cant be 0")
    elif quadrant_size % 2 is 1:
        raise ValueError("The Quadrant Size must be Divisable by 2")

    output = {}

    for quadrant in range(quadrant_size):
        output[quadrant] = generate_sector(sector_size, object_weight)

    return output


# TODO: Rewrite Print_Sector Code
def visualise_sector(mapdata: dict):
    """No Doc"""
    map_size = len(mapdata) + 1
    text = "|  | "
    for index in range(1, map_size):
        if index <= 9:
            text += f"0{index} "
        else:
            text += f"{index} "
    text += "|"
    seperator = "-" * len(text)

    print(seperator)
    print(text)
    print(seperator)

    counter = 1
    for map_data in mapdata.values():
        if counter <= 9:
            text = f"|0{counter}| "
        else:
            text = f"|{counter}| "
        counter += 1
        for position_data in map_data:
            if position_data is "*":
                position_data = Fore.YELLOW + position_data + Fore.RESET
            elif position_data in ["!", "C", "^"]:
                position_data = Fore.RED + position_data + Fore.RESET
            elif position_data is "B":
                position_data = Fore.GREEN + position_data + Fore.RESET
            elif position_data is "P":
                position_data = Fore.BLUE + position_data + Fore.RESET
            elif position_data is "#":
                position_data = Fore.LIGHTBLACK_EX + position_data + Fore.RESET
            text += f"{position_data}  "
        text += "|"
        print(text)

    print(seperator)
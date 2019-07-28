"""
An Util which has Utilitys to generate an Text Based Map

Contains:
    Generate Sector: An Map Generator which Generates an Weighted Map Grid
    Visualise Sector: Takes an Map Grid and Prints it out in an Human Readable form
"""

import bisect
import random

import colorama
from colorama import Fore

colorama.init()


# TODO: Make @ Guaranteed to be in there
def generate_sector(size: int, object_weight: list) -> dict:
    """
    Generates an Sector with Weighted Spawns

    Args:
        size: Int Representing the Size of the Sector (Size X Size)
        object_weight: An Nested List with Object / Value Types

    Examples:
        generate_sector(6, [["*", 50], ["#", 10]]) would output something like this

        ---------------------
        |  | 01 02 03 04 05 |
        ---------------------
        |01| *  *  *  *  *  |
        |02| *  *  *  *  #  |
        |03| *  *  *  *  #  |
        |04| *  *  *  #  *  |
        |05| *  #  *  *  #  |
        ---------------------

    Returns:
        An Dict with Lists inside which Represent the Map Data per Row
    """

    output = {}

    totals = []
    running_total = 0

    for w in object_weight:
        running_total += w[1]
        totals.append(running_total)

    for x in range(1, size):
        row = []
        for y in range(1, size):
            ran = random.random() * totals[-1]
            i = bisect.bisect_right(totals, ran)
            object = object_weight[i][0]
            row.append(object)
        output[x] = row
    return output


def generate_quadrant(size: int) -> dict:
    pass


# TODO: Rewrite Print_Sector Code
def visualise_sector(mapdata: dict):
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


print_sector(generate_sector(6, [["*", 50], ["#", 10]]))

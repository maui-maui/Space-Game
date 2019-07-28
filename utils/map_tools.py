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


# TODO: Make @ Guaranteed to be in there
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
            elif placed_player is True and object is "@":
                while object is "@":
                    object = next()
            row.append(object)
        output[x] = row
    return output


def generate_quadrant(size: int) -> dict:
    """Empty"""
    pass


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
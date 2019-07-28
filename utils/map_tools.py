"""
Tools for Generating Sectors and Quadrants

Contains:
    generate_sector - Generates an Sector
    generate_quadrant - Generates an Quadrant
    print_sector - Prints the Sector into the Console
"""

import random


# TODO: Add Error Catching when no @ got Generated
def generate_sector(size: int) -> dict:
    """
    Generates the Sector Map Data

    generate_sector(9) would generate an 9x9 Map

    Dict Structure:
        {
            0: [MapData]
            1: [MapData]
        \

    Warning: Keep in Mind that the dict and lists are zero indexed meaning 0 is the first value

    Parameters
    ----------
    size: Int Representing how Large the Map Grid should be

    Returns
    -------
    An Dict with Lists containing the Lists with the Row Data
    """

    output = {}
    player_set = False
    map_objects = ["#", "P", "C", "!", "^", "B", "@"]

    for x in range(size):
        row = []
        for y in range(size):
            random_object = random.choice(map_objects)
            random_int = random.randint(0, 5)

            # Prevents Multiple Player Locations to be Spawned
            if random_object is "@" and player_set is True:
                while random_object is "@":
                    random_object = random.choice(map_objects)
            elif random_object is "@" and player_set is False:
                row.append("@")
                player_set = True
                continue

            # Make Commanders less Common
            if random_object is "C":
                if random_int <= 2:
                    row.append("C")
                    continue
                else:
                    row.append("#")
                    continue

            # Make Enemy Bases less Common
            if random_object is "!":
                if random_int is 1:
                    row.append("!")
                    continue
                else:
                    row.append("#")
                    continue

            # Make Friendly Bases Less Common
            if random_object is "B":
                if random_int <= 2:
                    row.append("B")
                    continue
                else:
                    row.append("#")
                    continue

            row.append(random_object)
        output[x] = row

    return output


def generate_quadrant(size: int) -> dict:
    """
    Generates the Quadrant Map Data

    generate_sector(9) would generate an 9x9 Map

    Dict Structure:
        {
            Quadrant1: {Sector Data}
            Quadrant2: {Sector Data}
        \

    Parameters
    ----------
    size: Int Representing how Large the Map Grid should be

    Returns
    -------
    An Dict with Nested Dict containing the Sector Map Data
    """
    pass


def print_sector(mapdata: dict):
    """
    Prints the Map Data into the Console

    ---------------------
    |  | 1  2  3  4  5  |
    ---------------------
    | 1| P  B  *  P  C  |
    | 2| P  ^  P  C  P  |
    | 3| ^  *  @  *  ^  |
    | 4| P  *  *  ^  *  |
    | 5| P  !  P  ^  ^  |
    ---------------------

    Works with any Map Size

    Parameters
    ----------
    mapdata: dict An Dict Containing the Map Data (generate it with generate_sector)
    """

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
            text += f"{position_data}  "
        text += "|"
        print(text)

    print(seperator)
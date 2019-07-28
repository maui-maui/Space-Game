"""
Tools for Generating Sectors and Quadrants

Contains:
    generate_sector - Generates an Sector
    generate_quadrant - Generates an Quadrant
"""

import random


# TODO: Add Error Catching when no @ got Generated
def generate_sector(size: int) -> dict:
    """
    Generates the Sector Map Data

    generate_sector(9) would generate an 9x9 Map

    Dict Structure:
        {
            X!: [MapData]
            X2: [MapData]
        \

    Parameters
    ----------
    size: Int Representing how Large the Map Grid should be

    Returns
    -------
    An Dict with Lists containing the Map Data per Row
    """

    output = {}
    player_set = False
    map_objects = ["*", "P", "C", "!", "^", "B", "@"]

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
                    row.append("*")
                    continue

            # Make Enemy Bases less Common
            if random_object is "!":
                if random_int is 1:
                    row.append("!")
                    continue
                else:
                    row.append("*")
                    continue

            # Make Friendly Bases Less Common
            if random_object is "B":
                if random_int <= 2:
                    row.append("B")
                    continue
                else:
                    row.append("*")
                    continue

            row.append(random_object)
        output[f"X{x}"] = row

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


def parse_map(mapdata: list):
    pass

#!/usr/bin/python3
"""
Defines a function that determines if a box containing a list
of lists can be opened using keys stored in the lists
"""


def unlock(boxes):
    """Determines if boxes can be unlocked"""
    pos = 0
    unlk = {}

    for idx, box in enumerate(boxes):
        if len(box) == 0 or pos == 0:
            unlk[pos] = "always_unlocked"
        for key in box:
            if key < len(boxes) and key != pos:
                unlk[key] = key
        if len(unlk) == len(boxes):
            return True
        pos += 1
    return False

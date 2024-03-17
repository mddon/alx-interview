#!/usr/bin/python3
"""
Defines a function that determines if a box containing a list
of lists can be opened using keys stored in the lists
"""


def can_unlock_all(boxes):
    """Determines if boxes can be unlocked"""
    current_position = 0
    unlocked_boxes = {}

    for index, box in enumerate(boxes):
        if len(box) == 0 or current_position == 0:
            unlocked_boxes[current_position] = "always_unlocked"
        for key in box:
            if key < len(boxes) and key != current_position:
                unlocked_boxes[key] = key
        if len(unlocked_boxes) == len(boxes):
            return True
        current_position += 1
    return False

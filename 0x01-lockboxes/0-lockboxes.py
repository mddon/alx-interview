#!/usr/bin/python3
"""Determines if all boxes can be opened."""


def canUnlockAll(boxes):
    """ Determines if all boxes can be opened."""
    if not boxes:
        return False

    keys = {0}
    new_keys = set()

    while new_keys != keys:
        new_keys = keys.copy()
        for i, box in enumerate(boxes):
            if i in keys:
                keys.update(box)

    return len(keys) == len(boxes)

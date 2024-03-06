#!/usr/bin/python3
"""Script on Pascal Triangle for Mock Technical Interview"""


def pascal_triangle(n):
    """Returns a list of lists of numbers representing the Pascal triangle."""
    if n <= 0:
        return []

    pascal_triangle = []
    for i in range(n):
        row = [1] * (i + 1)
        if i > 1:
            for j in range(1, i):
                row[j] = pascal_triangle[i - 1][j - 1] + pascal_triangle[i - 1][j]
        pascal_triangle.append(row)

    return pascal_triangle

#!/usr/bin/python3
"""Write a script that reads stdin line by line and computes metrics"""
import sys

def print_stats(total_size, status_counts):
    """
    Method to print
    Args:
        dict_sc: dict of status codes
        total_file_size: total of the file
    Returns:
        Nothing
    """

    print("File size: {}".format(total_size))
    for code in sorted(status_counts.keys()):
        if status_counts[code] > 0:
            print("{}: {}".format(code, status_counts[code]))

total_size = 0
status_counts = {"200": 0, "301": 0, "400": 0, "401": 0, "403": 0, "404": 0, "405": 0, "500": 0}
line_counter = 0

try:
    for line in sys.stdin:
        parts = line.split()
        if len(parts) != 9:
            continue

        status_code = parts[-2]
        file_size = int(parts[-1])

        total_size += file_size

        if status_code in status_counts:
            status_counts[status_code] += 1

        line_counter += 1

        if line_counter == 10:
            print_stats(total_size, status_counts)
            line_counter = 0

except KeyboardInterrupt:
    print_stats(total_size, status_counts)

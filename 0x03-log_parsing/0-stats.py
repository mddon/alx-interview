#!/usr/bin/python3

import sys


def print_msg(dicts, total_size):
    """
    Method to print the file size and status code metrics.
    Args:
        total_size (int): Total size of the files processed.
        dicts (dict): Dictionary containing status codes
    Returns:
        None
    """

    print("File size: {}".format(total_size))
    for key, code in sorted(dicts.items()):
        if code != 0:
            print("{}: {}".format(key, code))

total_size = 0
line_counter = 0
program = 0
dicts = {"200": 0, "301": 0, "400": 0, "401": 0, "403": 0, "404": 0, "405": 0, "500": 0}

try:
    for line in sys.stdin:
        parts = line.split()  # Splitting the input line into parts
        parts = parts[::-1]

        if len(parts) > 2:   # Checking if the line has exactly 9 parts
            line_counter += 1

            if line_counter <= 10:
                total_size += int(parts[0])  # file size
                program = parts[1]  # status code

                if program in dicts: # Utilizing the status_counts variable
                    dicts[program] += 1

            if line_counter == 10:  # Printing statistics every 10 lines
                print_msg(dicts, total_size)
                line_counter = 0

finally:
    print_msg(dicts, total_size)  # Printing final statistics

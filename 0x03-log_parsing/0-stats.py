#!/usr/bin/python3
"""A script that reads stdin line by line, parses the input, and computes metrics."""

import sys

def print_msg(total_size, status_counts):
    """
    Function to print the file size and status code metrics.
    
    Args:
        total_size (int): Total size of the files processed.
        status_counts (dict): Dictionary containing status codes and their counts.
        
    Returns:
        None
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
        parts = line.split()  # Splitting the input line into parts
        if len(parts) != 9:   # Checking if the line has exactly 9 parts
            continue

        status_code = parts[-2]  # Extracting the status code
        file_size = int(parts[-1])  # Extracting the file size

        total_size += file_size  # Adding file size to the total

        if status_code in status_counts:  # Updating status code count
            status_counts[status_code] += 1

        line_counter += 1

        if line_counter == 10:  # Printing statistics every 10 lines
            print_msg(total_size, status_counts)
            line_counter = 0

finally:
    print_msg(total_size, status_counts)  # Printing final statistics

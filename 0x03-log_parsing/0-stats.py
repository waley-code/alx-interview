#!/usr/bin/python3
"""script that reads stdin line by line and computes metrics"""
import sys

# Variables to store the metrics
total_file_size = 0
status_code_counts = {}


try:
    line_count = 0
    for line in sys.stdin:
        line = line.strip()

        # Extract the relevant information from the line
        parts = line.split(' ')
        if len(parts) != 7:
            continue
        status_code = parts[5]
        file_size = int(parts[6])

        # Update the metrics
        total_file_size += file_size
        status_code_counts[status_code] = status_code_counts.get(status_code, 0) + 1

        line_count += 1

        # Print statistics every 10 lines
        if line_count % 10 == 0:
            print("Total file size:", total_file_size)
            sorted_status_codes = sorted(status_code_counts.keys(), key=lambda x: int(x))
            for code in sorted_status_codes:
                print(code + ":", status_code_counts[code])
            print()

except KeyboardInterrupt:
    # Handle keyboard interruption (CTRL + C)
    print("Total file size:", total_file_size)
    sorted_status_codes = sorted(status_code_counts.keys(), key=lambda x: int(x))
    for code in sorted_status_codes:
        print(code + ":", status_code_counts[code])


#!/usr/bin/python3
import sys
import signal
import re

total_size = 0
status_codes_count = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}
line_count = 0

def print_statistics():
    """Print the current statistics."""
    print(f"File size: {total_size}")
    for code in sorted(status_codes_count.keys()):
        if status_codes_count[code] > 0:
            print(f"{code}: {status_codes_count[code]}")

def signal_handler(sig, frame):
    """Handle keyboard interruption (CTRL + C)."""
    print_statistics()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

regex = re.compile(
    r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - \[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d+\] "GET /projects/260 HTTP/1.1" (.{3}) (\d+)'
)

try:
    for line in sys.stdin:
        line = line.strip()
        match = regex.fullmatch(line)
        if match:
            line_count += 1
            status_code = match.group(1)
            file_size = int(match.group(2))

            total_size += file_size

            if status_code in status_codes_count:
                status_codes_count[status_code] += 1

            if line_count % 10 == 0:
                print_statistics()

finally:
    print_statistics()

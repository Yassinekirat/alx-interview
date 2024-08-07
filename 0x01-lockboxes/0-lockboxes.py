#!/usr/bin/python3
from typing import List
"""Lockboxes"""


def canUnlockAll(boxes: List[List[int]]) -> bool:
    """Lockboxes"""
    n: int = len(boxes)
    # Determine the number of boxes
    opened: set = set()
    # Create a set to keep track of which boxes have been opened
    to_process: List[int] = [0]
    # Start processing with the first box (box 0), which is initially unlocked

    # Process each box in the queue
    while to_process:
        current_box: int = to_process.pop()  # Get a box from the queue

        if current_box not in opened:  # If the box has not been opened yet
            opened.add(current_box)  # Mark the box as opened

            # Check all keys in the current box
            for key in boxes[current_box]:
                if key < n:  # Ensure the key corresponds to a valid box
                    to_process.append(key)
                    # Add the box to the queue

    # Check if all boxes have been opened
    return len(opened) == n
# Return True if all boxes have been opened, otherwise False

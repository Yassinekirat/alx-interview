#!/usr/bin/python3
from typing import List


def canUnlockAll(boxes: List[List[int]]) -> bool:
    """
    Determine if all boxes can be unlocked.

    Args:
    boxes (List[List[int]]):
    A list of lists, where each sublist contains keys to other boxes.

    Returns:
    bool: True if all boxes can be opened, otherwise False.

    Steps:
    1. Determine the number of boxes (n).
    2. Create a set to keep track of which boxes have been opened (opened).
    3. Start processing with the first box (box 0),
        which is initially unlocked.
    4. Process each box in the queue (to_process):
        a. Get a box from the queue.
        b. If the box has not been opened yet:
            i. Mark the box as opened.
            ii. Check all keys in the current box.
            iii. For each key, if it corresponds to a valid box,
                add the box to the queue.
    5. Check if all boxes have been opened.
    6. Return True if all boxes have been opened, otherwise return False.
    """

    n: int = len(boxes)
    opened: set = set()
    to_process: List[int] = [0]

    while to_process:
        current_box: int = to_process.pop()

        if current_box not in opened:
            opened.add(current_box)

            for key in boxes[current_box]:
                if key < n:
                    to_process.append(key)

    return len(opened) == n

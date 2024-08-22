#!/usr/bin/python3
"""
Module to validate UTF-8 encoding
"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.

    Args:
        data (list): A list of integers representing bytes.

    Returns:
        bool: True if the data set is valid UTF-8, False otherwise.
    """
    try:
        masked_data = [byte & 0xFF for byte in data]
        bytes(masked_data).decode("utf-8")
        return True
    except UnicodeDecodeError:
        return False

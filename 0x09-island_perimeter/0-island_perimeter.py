#!/usr/bin/python3
"""Island Perimeter"""


def island_perimeter(grid):
    """Initialize the perimeter"""
    perimeter = 0

    # Get the dimensions of the grid
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    # Iterate over each cell in the grid
    for r in range(rows):
        for c in range(cols):
            # If the current cell is land
            if grid[r][c] == 1:
                # Check all 4 sides (up, down, left, right)
                # Check if the cell is
                # on the top edge or if the
                # cell above is water
                if r == 0 or grid[r - 1][c] == 0:
                    perimeter += 1

                # Check if the cell is
                # on the bottom edge or if the
                # cell below is water
                if r == rows - 1 or grid[r + 1][c] == 0:
                    perimeter += 1

                # Check if the cell is on the left edge
                # or if the cell to the left is water
                if c == 0 or grid[r][c - 1] == 0:
                    perimeter += 1

                # Check if the cell is on the right
                # edge or if the cell to the right
                # is water
                if c == cols - 1 or grid[r][c + 1] == 0:
                    perimeter += 1

    return perimeter

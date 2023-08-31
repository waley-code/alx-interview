#!/usr/bin/python3
"""function def island_perimeter(grid):
    returns the perimeter of the island described in grid
"""


def island_perimeter(grid):
    """returns the perimeter"""
    rows = len(grid)
    cols = len(grid[0])

    perimeter = 0

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                perimeter += 4  # Initialize with the full perimeter

                # Check neighbors
                if row > 0 and grid[row - 1][col] == 1:
                    perimeter -= 2  # Subtract top neighbor
                if col > 0 and grid[row][col - 1] == 1:
                    perimeter -= 2  # Subtract left neighbor

    return perimeter

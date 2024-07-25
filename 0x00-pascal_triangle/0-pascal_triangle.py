#!/usr/bin/python3
"""
0-pascal_triangle
"""


def pascal_triangle(n):
    """ creates a pascal triangle """
    if n <= 0:
        return []
    triangle = [[1]]
    for r in range(1,n):
        new_row = [1]
        for i in range(1,r):
            mid_raw = new_row.append(triangle[r-1][i-1] + triangle[r-1][i])
        end_raw = new_row.append(1)
        triangle.append(new_row)

    return triangle

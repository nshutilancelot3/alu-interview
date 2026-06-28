#!/usr/bin/python3
"""
Module for generating Pascal's triangle.
"""


def pascal_triangle(n):
    """
    Return a list of lists representing Pascal's triangle of n rows.

    Args:
        n (int): Number of rows.

    Returns:
        list: List of lists of integers, or empty list if n <= 0.
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        prev = triangle[i - 1]
        row = [1]
        for j in range(1, i):
            row.append(prev[j - 1] + prev[j])
        row.append(1)
        triangle.append(row)

    return triangle

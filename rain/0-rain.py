#!/usr/bin/python3
"""
Module to calculate the total rainwater retained between walls.
"""


def rain(walls):
    """
    Calculate how many square units of water will be retained after rain.

    For each position i, the water retained equals:
        min(max height to the left, max height to the right) - walls[i]

    Two prefix arrays are built in O(n) time so the overall complexity
    is O(n) time and O(n) space.

    Args:
        walls (list): Non-negative integers representing wall heights.

    Returns:
        int: Total square units of rainwater retained.
             Returns 0 if the list is empty.
    """
    if not walls:
        return 0

    n = len(walls)

    left_max = [0] * n
    right_max = [0] * n

    left_max[0] = walls[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i - 1], walls[i])

    right_max[n - 1] = walls[n - 1]
    for i in range(n - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], walls[i])

    total = 0
    for i in range(n):
        total += min(left_max[i], right_max[i]) - walls[i]

    return total

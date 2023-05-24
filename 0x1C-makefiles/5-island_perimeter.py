
Oghenet3ga
/
alx-low_level_programming
Public
Code
Issues
Pull requests
Actions
Projects
Security
Insights
Breadcrumbsalx-low_level_programming/0x1C-makefiles
/5-island_perimeter.py
Latest commit
Oghenet3ga
Oghenet3ga
9 hours ago
History
28 lines (23 loc) · 744 Bytes
Breadcrumbsalx-low_level_programming/0x1C-makefiles
/5-island_perimeter.py
File metadata and controls

Code

Blame
#!/usr/bin/python3
"""Defines an island perimeter measuring function."""
def island_perimeter(grid):
    """Return the perimiter of an island.
    The grid represents water by 0 and land by 1.
    Args:
        grid (list): A list of list of integers representing an island.
    Returns:
        The perimeter of the island defined in grid.
    """
    width = len(grid[0])
    height = len(grid)
    edges = 0
    size = 0
    for i in range(height):
        for j in range(width):
            if grid[i][j] == 1:
                size += 1
                if (j > 0 and grid[i][j - 1] == 1):
                    edges += 1
                if (i > 0 and grid[i - 1][j] == 1):
                    edges += 1
    return size * 4 - edges * 2

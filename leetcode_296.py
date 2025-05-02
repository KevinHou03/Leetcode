def minTotalDistance(grid):
    if not grid or not grid[0]:
        return 0

    rows, cols = len(grid), len(grid[0])
    x_coords, y_coords = []

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                x_coords.append(r)
                y_coords.append(c)

    def median(lst):
        lst.sort()
        return lst[len(lst) // 2]

    x_median = median(x_coords)
    y_median = median(y_coords)

    total_x_distance = 0
    total_y_distance = 0

    for x in x_coords:
        total_x_distance += abs(x - x_median)

    for y in y_coords:
        total_y_distance += abs(y - y_median)

    total_distance = total_x_distance + total_y_distance

    return total_distance

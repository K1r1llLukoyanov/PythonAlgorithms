from collections import deque


def dist_grid(grid, source, target=None):
    rows = len(grid)
    cols = len(grid[0])
    i, j = source
    grid[i][j] = 's'
    Q = deque()
    Q.append(source)
    while Q:
        i1, j1 = Q.popleft()
        for di, dj, symbol in [(0, +1, '>'), (0, -1, '<'), (+1, 0, 'v'), (-1, 0, '^')]:
            i2 = i1 + di
            j2 = j1 + dj
            if not (0 <= i2 <= rows and 0 <= j2 < cols):
                continue
            if grid[i2][j2] != ' ':
                continue
            grid[i2][j2] = symbol
            if (i2, j2) == target:
                grid[i2][j2] = 't'
                return
            Q.append((i2, j2))


def main():
    pass


if __name__ == "__main__":
    main()

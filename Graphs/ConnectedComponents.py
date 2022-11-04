
#   Using DFS
def dfs_grid(grid, i, j, mark, free="#"):
    grid[i][j] = mark
    height = len(grid)
    width = len(grid[0])
    for ni, nj in [(i-1, j), (i+1, j), (i, j+1), (i, j-1)]:
        if 0 <= ni < height and 0 <= nj < width and grid[ni][nj] == free:
            dfs_grid(grid, ni, nj, mark, free)


def count_components_grid(grid, free="#"):
    components = 0
    height = len(grid)
    width = len(grid[0])
    for i in range(height):
        for j in range(width):
            if grid[i][j] == free:
                components += 1
                dfs_grid(grid, i, j, str(components), free)

    return components


def main():
    grid = [['#', 'X'], ['X', '#']]
    comp_count = count_components_grid(grid)
    print(grid)
    print(comp_count)


if __name__ == "__main__":
    main()

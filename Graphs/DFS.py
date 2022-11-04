from graph import Graph


#   Recursive Depth First Search
def dfs_recursive(graph, node, seen):
    seen[node] = True
    print(graph.node2name[node])
    for neighbor in graph[node]:
        if not seen[neighbor]:
            dfs_recursive(graph, neighbor, seen)


#   Iterative Depth First Search
def dfs_iterative(graph, start, seen):
    seen[start] = True
    to_visit = [start]
    while len(to_visit):
        node = to_visit.pop()
        print(graph.node2name[node])
        for next in graph[node]:
            if not seen[next]:
                seen[next] = True
                to_visit.append(next)


#   Depth First Search on 2d grid
def dfs_grid(grid, i, j, mark='X', free='.'):
    height = len(grid)
    width = len(grid[0])
    to_visit = [(i, j)]
    grid[i][j] = mark
    while to_visit:
        i1, j1 = to_visit.pop()
        for i2, j2 in [(i1 + 1, j1), (i1-1, j1), (i1, j1+1), (i1, j1-1)]:
            if 0 <= i2 < height and 0 <= j2 < width and grid[i2][j2] == free:
                to_visit.append((i2, j2))
                grid[i2][j2] = mark


def main():
    gr = Graph()
    gr.add_node('Kazan')
    gr.add_node('Nizhnekams')
    gr.add_edge('Kazan', 'Nizhnekams', 350)
    seen = [False for _ in range(len(gr))]
    dfs_recursive(gr, 0, seen)
    seen = [False for _ in range(len(gr))]
    dfs_iterative(gr, 0, seen)


    grid = [['.', 'Y', '.']]
    dfs_grid(grid, 0, 0)
    print(grid)

if __name__ == "__main__":
    main()

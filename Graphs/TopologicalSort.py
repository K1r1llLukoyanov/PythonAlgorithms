from graph import Graph


#   Graph Topological Sort
def topological_order_dfs(graph):
    n = len(graph)
    order = []
    times_seen = [-1]*n
    for start in range(n):
        if times_seen[start] == -1:
            times_seen[start] == 0
            to_visit = [start]
            while to_visit:
                node = to_visit[-1]
                children = graph[node]
                if times_seen[node] == len(children):
                    to_visit.pop()
                    order.append(node)
                else:
                    child = children[times_seen[node]]
                    times_seen[node] += 1
                    if times_seen[child] == -1:
                        times_seen[child] = 0
                        to_visit.append(child)
    return order[::-1]


#   Greedy Topological Sort
def topological_order(graph):
    V = range(len(graph))
    indeg = [0 for _ in V]
    for node in V:
        for n in graph[node]:
            indeg[n] += 1
    Q = [node for node in V if indeg[node] == 0]

    order = []

    while Q:
        node = Q.pop()
        order.append(node)
        for neighbor in graph[node]:
            indeg[neighbor] -= 1
            if indeg[neighbor] == 0:
                Q.append(neighbor)

    return order


def main():
    graph = Graph()
    graph.add_node(1)
    graph.add_node(2)
    graph.add_node(3)
    graph.add_node(4)
    graph.add_node(5)

    graph.add_edge_directed(1, 5, 1)
    graph.add_edge_directed(1, 2, 1)
    graph.add_edge_directed(5, 4, 1)
    graph.add_edge_directed(5, 2, 1)
    graph.add_edge_directed(3, 1, 1)

    order = topological_order(graph)

    for o in order:
        print("{} ".format(graph.node2name[o]), end='')  # 3 1 5 4 2


if __name__ == "__main__":
    main()

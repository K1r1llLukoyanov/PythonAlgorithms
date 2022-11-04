from graph import Graph


#   To find cut nodes or articulate vertices and cut edges or bridges
def cut_nodes_edges(graph):
    n = len(graph)
    time = 0
    num = [None]*n
    low = [n]*n
    parent = [None]*n
    critical_children = [0]*n
    times_seen = [-1]*n
    for start in range(n):
        if times_seen[start] == -1:
            times_seen[start] = 0
            to_visit = [start]
            while to_visit:
                node = to_visit[-1]
                if times_seen[node] == 0:
                    num[node] = time
                    time += 1
                    low[node] = float('inf')
                children = graph[node]
                if times_seen[node] == len(children):
                    to_visit.pop()
                    up = parent[node]
                    if up is not None:
                        low[up] = min(low[up], low[node])
                        if low[node] >= num[up]:
                            critical_children[up] += 1
                else:
                    child = children[times_seen[node]]
                    times_seen[node] += 1
                    if times_seen[child] == -1:
                        parent[child] = node
                        times_seen[child] = 0
                        to_visit.append(child)
                    elif num[child] < num[node] and parent[node] != child:
                        low[node] = min(low[node], num[child])
    cut_edges = []
    cut_nodes = []
    for node in range(n):
        if parent[node] is None:
            if critical_children[node] >= 2:
                cut_nodes.append(node)
        else:
            if critical_children[node] >= 1:
                cut_nodes.append(node)
            if low[node] >= num[node]:
                cut_edges.append((parent[node], node))

    return cut_nodes, cut_edges


def main():
    graph = Graph()
    graph.add_node('Kazan')
    graph.add_node('Nizhnekamsk')
    graph.add_node('Chelny')
    graph.add_edge('Kazan', 'Nizhnekamsk', 350)
    graph.add_edge('Nizhnekamsk', 'Chelny', 60)
    cut_nodes, cut_edges = cut_nodes_edges(graph)
    print(cut_edges)
    print(cut_nodes)


if __name__ == "__main__":
    main()

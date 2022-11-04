from graph import Graph


#   Finding Strongly Connected Components
def tarjan_recursif(graph):
    global sccp, waiting, dfs_time, dfs_num
    sccp = []
    waiting = []
    waits = [False] * len(graph)
    dfs_time = 0
    dfs_num = [None] * len(graph)

    def dfs(node):
        global sccp, waiting, dfs_time, dfs_num
        waiting.append(node)
        waits[node] = True
        dfs_num[node] = dfs_time
        dfs_time += 1
        dfs_min = dfs_num[node]
        for neighbor in graph[node]:
            if dfs_num[neighbor] is None:
                dfs_min = min(dfs_min, dfs(neighbor))
            elif waits[neighbor] and dfs_min > dfs_num[neighbor]:
                dfs_min = dfs_num[neighbor]
        if dfs_min == dfs_num[node]:
            sccp.append([])
            while True:
                u = waiting.pop()
                waits[u] = False
                sccp[-1].append(u)
                if u == node:
                    break
        return dfs_min

    for node in range(len(graph)):
        if dfs_num[node] is None:
            dfs(node)

    return sccp


def main():
    graph = Graph()
    graph.add_node('Kazan')
    graph.add_node('Nizhnekamsk')
    graph.add_node('Chelny')
    graph.add_edge_undirected('Kazan', 'Nizhnekamsk', 350)
    graph.add_edge_undirected('Nizhnekamsk', 'Chelny', 60) 
    graph.add_edge_undirected('Kazan', 'Chelny', 420)
    sccp = tarjan_recursif(graph)
    for i, comp in enumerate(sccp):
        print("Component {}: ".format(i+1), end='')
        for node in range(len(comp)-1):
            print("{} - ".format(graph.node2name[comp[node]]), end='')
        print(graph.node2name[comp[len(comp)-1]])


if __name__ == "__main__":
    main()

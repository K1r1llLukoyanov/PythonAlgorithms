def floyd_warshall(weight):
    V = range(len(weight))
    for k in V:
        for u in V:
            for v in V:
                weight[u][v] = min(weight[u][v], weight[u][k] + weight[k][v])
    for v in V:
        if weight[v][v] < 0:    # negative cycle detected
            return True
    return False
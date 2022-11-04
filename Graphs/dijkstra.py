from heapq import heappop, heappush
from ourheap import OurHeap
from graph import Graph


def dijkstra(graph, weight, source=0, target=None):
    n = len(graph)
    assert all(weight[u][v] > 0 for u in range(n) for v in graph[u])
    prec = [None] * n
    black = [False] * n
    dist = [float('inf')] * n
    dist[source] = 0
    heap = [(0, source)]

    while heap:
        dist_node, node = heappop(heap)
        if not black[node]:
            black[node] = True
            if node == target:
                break
            for neighbor in graph[node]:
                dist_neighbor = dist_node + weight[node][neighbor]
                if dist[neighbor] > dist_neighbor:
                    dist[neighbor] = dist_neighbor
                    prec[neighbor] = node
                    heappush(heap, (dist_neighbor, neighbor))
    return dist, prec


def dijkstra_update_heap(graph: Graph, weight, source=0, target=None):
    n = len(graph)
    assert all(weight[u][v] > 0 for u in range(n) for v in graph[u])
    prec = [None] * n
    dist = [float('inf')] * n
    dist[source] = 0
    heap = OurHeap([(dist[node], node) for node in range(n)])
    while heap:
        dist_node, node = heap.pop()
        if node == target:
            break
        for neighbor in graph[node]:
            old = dist[neighbor]
            new = dist_node + weight[node][neighbor]
            if new < old:
                dist[neighbor] = new
                prec[neighbor] = node
                heap.update((old, neighbor), (new, neighbor))
    return dist, prec



def main():
    graph = Graph()
    graph.add_node('Kazan')
    graph.add_node('Nizhnekamsk')
    graph.add_node('Chelny')
    graph.add_edge_undirected('Kazan', 'Nizhnekamsk', 350)
    graph.add_edge_undirected('Nizhnekamsk', 'Chelny', 60)
    graph.add_edge_undirected('Kazan', 'Chelny', 420)
    weigth = graph.weight
    start = 0
    finish = 2
    dist, prec = dijkstra_update_heap(graph, weigth, start, finish)
    i = prec[-1]
    print('Way: ', end='')
    print(graph.node2name[finish], end='')
    while i is not None:
        print(" <- {} ".format(graph.node2name[i]), end='')
        i = prec[i]
    print("\nMin distance from {} to {} is {}".format(graph.node2name[start],
                                                      graph.node2name[finish], dist[finish]))


if __name__ == "__main__":
    main()

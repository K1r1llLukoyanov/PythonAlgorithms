from collections import deque
from graph import Graph

#   Iterative Breath First Search
def BFS(graph, start=0):
    to_visit = deque()
    dist = [float('inf')] * len(graph)
    prec = [None] * len(graph)
    dist[start] = 0
    to_visit.appendleft(start)
    while to_visit:
        node = to_visit.pop()
        for neighbor in graph[node]:
            if dist[neighbor] == float('inf'):
                dist[neighbor] = dist[node] + 1
                prec[neighbor] = node
                to_visit.appendleft(neighbor)
    return dist, prec

def main():
    gr = Graph()
    gr.add_node('Kazan')
    gr.add_node('Nizhnekams')
    gr.add_edge('Kazan', 'Nizhnekams', 350)
    dist, prec = BFS(gr)
    print(dist)
    print(prec)

if __name__ == "__main__":
    main()
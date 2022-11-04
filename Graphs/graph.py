from typing import List, Any, Dict

class Graph():
    def __init__(self) -> None:
        self.neighbours: List[List[Any]] = []
        self.name2node: Dict[Any, int] = {}
        self.node2name: List[Any] = []
        self.weight: List[List[int]] = []

    def __len__(self) -> int:
        return len(self.node2name)
    
    def __getitem__(self, v) -> int:
        return self.neighbours[v]

    def add_node(self, name) -> int:
        assert name not in self.name2node
        self.name2node[name] = len(self.name2node)
        self.node2name.append(name)
        self.neighbours.append([])
        self.weight.append({})
        return self.name2node[name]

    def add_edge_undirected(self, name_u, name_v, weight_uv = None) -> None:
        self.add_arc(name_u, name_v, weight_uv)
        self.add_arc(name_v, name_u, weight_uv)

    def add_edge_directed(self, name_u, name_v, weight_uv = None) -> None:
        self.add_arc(name_u, name_v, weight_uv)

    def add_arc(self, name_u, name_v, weight_uv = None) -> None:
        u = self.name2node[name_u]
        v = self.name2node[name_v]
        self.neighbours[u].append(v)
        self.weight[u][v] = weight_uv

    def print(self):
        for a in range(len(self.neighbours)):
            for b in self.neighbours[a]:
                print("{} -- {} -> {}".format(self.node2name[a], 
                self.weight[a][b], self.node2name[b]))
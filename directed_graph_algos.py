from collections import defaultdict


class DirectedGraph(object):
    def __init__(self, V, E, W = None):
        """

        :param V: List of vertices
        :param E: List of edges, where an edge e \in E is a tuple (u, v) for edge u -> v
        :param W: (Optional) Weight list for edges, where W_i is the weight of edge E_i. If not given, a default weight of 1.0 is assigned to every edge
        """
        if not W:   W = [1.0] * len(E)
        # Construct the graph in form of adjacency list.
        #   - For key u, value is a set of tuples (v, w) where v is the tail of edge u -> v with weigh w
        self.G = defaultdict(set)
        for u in V:
            self.G[u] = set()
        for e, w in zip(E, W):
            u, v = e
            self.G[u].add((v, w))

    def getTopologicalSort(self, G):
        topoSort = []
        visited = {v: False for v in G.keys()}

        def explore(u):
            visited[u] = True
            for v, _ in G[u]:
                if not visited[v]:
                    explore(v)
            topoSort.append(u)

        for u in G.keys():
            if not visited[u]:
                explore(u)
        return topoSort

    def getReverseGraph(self, G):
        Grev = defaultdict(set)
        for u in G.keys():
            Grev[u] = set()
        for u in G.keys():
            for v, w in G[u]:
                Grev[v].add((u, w))
        return Grev

    def getSCC(self, G):
        Grev = self.getReverseGraph(G)
        topoSort = self.getTopologicalSort(Grev) # topo-sort of reversed graph has sinks toward the tail of list
        reversed_topoSort = topoSort[::-1] # now sinks are toward the head of list
        # initializations
        CC, SCC, visited = 0, {}, {}
        for i, v in enumerate(G.keys()):
            SCC[v] = i
            visited[v] = False

        def explore(u, CC):
            """explore u when current Connected Component number is CC"""
            visited[u] = True
            SCC[u] = CC
            for v, _ in G[u]:
                if not visited[v]:
                    explore(v, CC)

        for u in reversed_topoSort:
            if not visited[u]:
                CC += 1
                explore(u, CC)
        return SCC

if __name__ == "__main__":
    V = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L']
    E = [('A', 'B'),
         ('B', 'D'),
         ('B', 'E'),
         ('E', 'B'),
         ('B', 'C'),
         ('C', 'F'),
         ('F', 'G'),
         ('G', 'F'),
         ('G', 'C'),
         ('F', 'I'),
         ('H', 'J'),
         ('J', 'H'),
         ('H', 'I'),
         ('I', 'J'),
         ('J', 'K'),
         ('K', 'L'),
         ('L', 'I'),
         ('E', 'L')]
    dg = DirectedGraph(V, E)
    print dg.getTopologicalSort(dg.G)
    print dg.getSCC(dg.G)


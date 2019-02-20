
class UnionFind:
    def __init__(self, N):
        """Define UnionFind data structure for N vertices"""
        self.root = [i for i in range(N)] # each vertex is in its own connected component
        self.sizeOf = [1 for i in range(N)] # initialize size of each component = 1

    def union(self, i, j):
        """create an edge between vertices labeled i and j.
        Basically join connected components containing vertices i and j"""
        # find root of vertices i and j
        # if different, merge smaller into larger one.
        pass

    def find(self, i):
        """find root of connected component containing vertex i"""
        # perform path compression while finding the root (make parent(i) <- parent(parent(i)) )
        pass

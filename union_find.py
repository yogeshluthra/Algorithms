
class UnionFind:
    def __init__(self, N):
        """Define UnionFind data structure for N vertices"""
        self.parentOf = [i for i in range(N)] # each vertex is in its own connected component
        self.sizeOf = [1 for i in range(N)] # initialize size of each component = 1
        self.CC = N # Number of connected components

    def union(self, i, j):
        """create an edge between vertices labeled i and j.
        Basically join connected components containing vertices i and j"""
        # find root of vertices i and j
        root_i, root_j = self.find(i), self.find(j)

        if not self._isSame(root_i, root_j):
        # if different, merge smaller into larger one.
            if self._treeSizeOf(root_i) > self._treeSizeOf(root_j):
                self._mergeInto(root_i, root_j)
            else:
                self._mergeInto(root_j, root_i)

    def find(self, i):
        """find root of connected component containing vertex i"""
        # perform path compression while finding the root (make parent(i) <- parent(parent(i)) )
        while not self._isSame(i, self._parentOf(i)):
            grandParent_i = self._parentOf(self._parentOf(i))
            self._setParentOf(i, grandParent_i) # path compression
            i = self._parentOf(i)
        return i

    def _isSame(self, i, j):
        return i == j

    def _treeSizeOf(self, root):
        return self.sizeOf[root]

    def _mergeInto(self, root_i, root_j):
        """merge tree rooted at root_j into tree rooted at root_i"""
        self._setParentOf(root_j, root_i)
        self.sizeOf[root_i] += self.sizeOf[root_j]
        self.CC -= 1

    def _parentOf(self, i):
        return self.parentOf[i]

    def _setParentOf(self, i, j):
        """set parent of i as j"""
        self.parentOf[i] = j

if __name__ == "__main__":
    uf = UnionFind(6)
    print uf.parentOf
    uf.union(0,4)
    print uf.parentOf
    uf.union(1,5)
    print uf.parentOf
    uf.union(1,2)
    print uf.parentOf
    uf.union(0,5)
    print uf.parentOf



class MinHeap(object):
    def __init__(self, l = []):
        self.h = [None] + l # 1 indexed
        self._heapify()

    def _sizeOfHeap(self):
        return len(self.h) - 1

    def _heapify(self):
        """heapify in-place."""
        pass

    def push(self, e):
        """push element e onto heap"""
        # Idea: insert at bottom and swim up
        self.h.append(e)
        self._swim(self._sizeOfHeap())

    def pop(self):
        """pop min element from the heap l"""
        # Idea: exchange top and last element. Then sink the top element.
        self._exch(1, self._sizeOfHeap())
        minE = self.h.pop()
        self._sink(1)
        return minE

    def pushpop(self, e):
        """push an element e onto heap l and pop min element after that"""
        self.push(e)
        minE = self.pop()
        return minE

    def _sink(self, i):
        """sink from index i"""
        while 2 * i <= self._sizeOfHeap():
            j = 2 * i
            if j < self._sizeOfHeap() and self._greater(j, j + 1): # if h[j] > h[j + 1]
                j = j + 1
            if not self._greater(i, j): # if h[i] < h[j], nothing to do. break
                break
            self._exch(i, j)
            i = j

    def _swim(self, i):
        """swim from index i"""
        while i > 1 and self._greater(i / 2, i): # if h[i/2] > h[i]
            self._exch(i / 2, i)
            i = i / 2

    def _greater(self, i, j):
        return self.h[i] > self.h[j]

    def _exch(self, i, j):
        t = self.h[i]
        self.h[i] = self.h[j]
        self.h[j] = t

if __name__ == "__main__":
    import random
    stream = range(1,11)
    random.shuffle(stream)
    print stream
    h = MinHeap()
    for i in range(len(stream)):
        h.push(stream[i])
    for i in range(len(stream)):
        print h.pop()



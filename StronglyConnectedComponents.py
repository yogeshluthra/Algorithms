import sys
import gc

sys.setrecursionlimit(1000000)
sys._debugmallocstats()
def trace(frame, event, arg):
    print("%s, %s:%d" % (event, frame.f_code.co_filename, frame.f_lineno))
    return trace
sys.settrace(trace)
gc.enable()
gc.collect()

class SCC(object):
    def __init__(self, edgeFile, n):
        """

        :param edgeFile: file containing edges
        :param n: number of vertices
        """
        self.n=n
        # - contruct Reverse graph
        Grev = [[] for _ in range(self.n)]
        with open(edgeFile) as f:  # each line contains 'A B', representing an edge from A->B
            for line in f:
                edge = list(map(int, line.strip().split(' ')))
                # - add reverse edge in graph, Grev
                Grev[edge[1]].append(edge[0])
        # - run DFSLoop in Grev and get Topological sorting of nodes for next operation
        print('Running reverse graph')
        self.topoSort=[]
        self.explored = [False] * self.n
        self.leaders = {}  # name of leaders of SCCs as key and corresponding elements in SCC as values
        self.DFSLoop(Grev, [i for i in range(self.n)], find_topo=True)
        Grev=None

        # - contruct Forward graph
        G = [[] for _ in range(self.n)]
        with open(edgeFile) as f:  # each line contains 'A B', representing an edge from A->B
            for line in f:
                edge = list(map(int, line.strip().split(' ')))
                # - add edge in the graph, G
                G[edge[0]].append(edge[1])
        # - then run DFSLoop in G, using topological sorting done on Grev
        print('Running forward graph')
        self.explored = [False] * self.n
        self.leaders = {}  # name of leaders of SCCs as key and corresponding size of SCC as values
        self.DFSLoop(G, self.topoSort, find_topo=False)

    def DFSLoop(self, G, exploreOrder, find_topo=False):
        """
        :param G: Graph
        :return:
        """
        while exploreOrder:
            len1=len(exploreOrder)
            s=exploreOrder.pop()
            if not self.explored[s]:
                self.leaders[s]=0
                print('running for leader', s)
                self.DFS(G, s, s, find_topo=find_topo)
            len2=len(exploreOrder)
            assert len2<len1

    def DFS(self, G, i, s, find_topo=False):
        """
        :param G: Graph
        :param i: Explore G starting at node i, with leader node=s
        :param s: leader node of this DFS run
        :return:
        """
        self.explored[i]=True
        # self.leaders[s].append(i)
        self.leaders[s] +=1
        for tailNode in G[i]:
            if not self.explored[tailNode]:
                print('tailNode',tailNode)
                self.DFS(G, tailNode, s, find_topo=find_topo)
        if find_topo:
            self.topoSort.append(i)
            print(len(self.topoSort))

    def printGraph(self, G):
        for i in range(self.n):
            if G[i]!=[]:
                print(i,':',G[i])

def main():
    n=875714+1
    edgeFile='data/SCC.txt'
    # n=9+1
    # edgeFile='data/SCC_test_small.txt'
    scc=SCC(edgeFile, n)
    print(scc.leaders)

sys.settrace(trace)
main()



